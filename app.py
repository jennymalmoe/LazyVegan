import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# CONFIGURATION
app = Flask(__name__)
# passing Mongo db uri via environment
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# passing Secret key via environment
app.secret_key = os.environ.get("SECRET_KEY")

# creating Mongo app
mongo = PyMongo(app)


# home page (binds function to url)
@app.route("/")
@app.route("/home")
def home():
    home = mongo.db.home.find()
    return render_template("home.html", home=home)


# recipe page
@app.route("/get_recipe")
def get_recipe():
    recipes = mongo.db.recipe.find()
    return render_template("recipe.html", recipes=recipes)


# search page
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipe.find({"$text": {"$search": query}}))
    return render_template("recipe.html", recipes=recipes)


# shop page
@app.route("/shop")
def shop():
    home = mongo.db.shop.find()
    return render_template("shop.html", shop=shop)


# register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("registration successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# log in page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        session["user_id"] = str(existing_user["_id"])
                        print(session)
                        flash("welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password 
                flash("incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        recipes = list(mongo.db.recipe.find({'created_by_name': username}))
        return render_template("profile.html",
        username=username, recipes=recipes)
        
    return redirect(url_for("login"))


# log out page
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add recipe page
@app.route("/add_recipe.html", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        gluten_free = "Gluten Free" if request.form.get("gluten_free") else "Contains Gluten"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_img": request.form.get("recipe_img"),
            "recipe_url": request.form.get("recipe_url"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_directions": request.form.get("recipe_directions"),
            "gluten_free": gluten_free, 
            "created_by_id": session["user_id"],
            "created_by_name": session["user"]
        }
        print(session)
        mongo.db.recipe.insert_one(recipe)
        flash("recipe successfully added")
        
        return redirect(url_for("get_recipe"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# edit recipe page
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        gluten_free = "on" if request.form.get("gluten_free") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_img": request.form.get("recipe_img"),
            "recipe_url": request.form.get("recipe_url"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_directions": request.form.get("recipe_directions"),
            "gluten_free": gluten_free, 
            "created_by_id": session["user_id"],
            "created_by_name": session["user"]
        }
        mongo.db.recipe.update({"_id": ObjectId(recipe_id)}, submit)
        flash("recipe successfully updated")
         
    # retrieve recipe from db   
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


# delete 
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipe.delete_one({"_id": ObjectId(recipe_id)})
    flash("recipe successfully deleted")
    return redirect(url_for("get_recipe"))


# recipe
@app.route("/recipe/<recipe_id>", methods=["GET", "POST"])
def recipe(recipe_id):

    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_details.html", recipe=recipe)


# How and where to run app
# Don't forget to change from True to False when submitting and deploying 
if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT")),
            debug=True)
