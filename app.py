import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipe")
def get_recipe():
    recipe = mongo.db.recipe.find()
    return render_template("recipe.html", recipe=recipe)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


# How and where to run app. 
# Don't forget to change from True to False when submitting and deploying. 
if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT")),
            debug=True)
