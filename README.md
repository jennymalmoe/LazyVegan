# Lazy Vegan Fast Food Recipes!
[View live website here!](https://jennymalmoe.github.io/###/)

[View GitHub repository here!](https://github.com/jennymalmoe/###)

![site on different devices](static/images/mock_up.png) 

Super quick recipes for when you're feeling lazy.



## Table of contents

___

1. [**User Experience**](#ux)
    * Project Goals
    * Business Goals
    * User Goals
    * User Stories
    * Design Choices
        * Color scheme
        * Typography
        * Imagery
        * Icons
    * Wireframes

2. [**Features**](#features)
    * Existing Features
    * Features Left to Implement

3. [**Database Design**](#database-design)

4. [**Technologies Used**](#technologies-used)
    * Languages 
    * Frameworks, Libraries & Programs

5. [**Testing**](#testing)
    * Testing User Stories from User Experience (UX) Section
    * Further Testing
    * Known Bugs

6. [**Deployment**](#deployment)
    * GitHub Pages
    * Forking the GitHub Repository
    * Making a Local Clone

7. [**Credits**](#credits)
    * Code 
    * Content
    * Media
    * Acknowledgements

# UX
## Project Goals
The purpose of this project is to *"...build a full-stack site that allows your users to manage a common dataset about a particular domain"* using HTML, CSS, JavaScript, Python+Flask, MongoDB and possible additional libraries and external APIs.

## Business Goals
Create a web application that allows users to:
    
* Add their own recipes to the website (CREATE)
* Find free recipes online (READ)
* Edit their recipes (UPDATE)
* Delete their recipes (DELETE)
    
In addition to the goals above; also to promote a brand of natural, eco-friendly and sustainable kitchen ware that goes hand in hand with Lazy Vegan approach. 

Eventually the recipe database will increase in both recipes and users/visitors. The site offer users to interact by adding their own recipes that makes the user feel like being a part of "the community". The site promotes the vegan life style, showing that it doesn't have to be that hard to eat, even junk food that are vegan. 

## User Goals
Find and share recipes, get inspired by the recipes and get inspired to add own recipes by the site which is signals a that a healty lifestyle doesn't have to be difficult. These easy recipes is done with minimal effort and is ready in no time! 

## User Stories

* First Time Visitor Goals

    * As a first time visitor, I want to easily grasp the sites purpose.
    * As a first time visitor, I want to find easy vegan fast food recipes.
    * As a first time visitor, I want to be inspired by the site, the recipes and the design. Get a positive feel. 
    * As a first time visitor, I want the site navigation to be intutive, user friendly and over all ease-of-use.
    * As a first time visitor, I want to be able to register as a new user.
    * As a first time visitor, I want to be able to log in and out (since I registered).
    * As a first time visitor, I want to be able to read the recipes (added by siteowner and users).
    * As a first time visitor, I want to be able to search for recipes.
    * As a first time visitor, I want to add recipes.
    * As a first time visitor, I want to be able to edit/update the recipes I've added. 
    * As a first time visitor, I want to be able to delete recipes I've added.
    * As a first time visitor, I want to locate their social media links to be able to follow and get  a feel for the credibility of the site. 

* Returning Visitor Goals

    * As a returning visitor, I want to be able to easily register if I didn't last time visiting. 
    * As a returning visitor, I want to be able to easily log in, if I registered last time visiting. 
    * As a returning visitor, I want to be able to read, add, update, delete and search for recipes.
    * As a returning visitor, I want to be able to reach out to siteowner for possibel collaboration or businessdeals.  

* Frequent Visitor Goals

    * As a frequent visitor, I want to check to see if there are any newly added recipes.

## Design Choices

* Color scheme

    The page consists of a white base with black and light green as secondary colors. Text and elements such as call to actions buttons and icons are black to make the text/information stand out and be as clear as possible. When hover buttons, they turn to the light green color to tie different elements of the sites together. The chosen colour scheme was specifically selected in order to define the vibe of the page. 

    Green is usually associated with healthy, organic and vegetarian food. The green and white color combination is clean, crisp, and are associated with nature and environmental awareness. The green color has a warm vibe while the supporting soft white lend a modern look. 
    
    Since green is found commonly in nature, it makes it an excellent choice for recipes sites with healthy and plant based foods. Many Health food stores, Salad bars and Vegan restaurants chooses these kind of colors.

    ![site on different devices](static/images/color_scheme.png)

* Typography

    Roboto font is the main font used throughout the site with Major Mono Display as headers font. Roboto has a mechanical skeleton and the forms are largely geometric. At the same time, the font features friendly and open curves. It's subtle and it doesn´t take any attention away from the content. This makes Roboto a more natural reading rhythm more commonly found in humanist and serif types. 
    
    Major Mono Display is a monospaced geometric sans serif all-uppercase typeface which also has a complete set of constructivist display characters with a playful attitude. This font is a great choice for playful web typography, especially at large point-sizes. Major Mono Display is a clean but charmig and unconventional font that also gives the site a relaxed vibe. The combination of these fonts represents both the healthy, vegan side aswell as the relaxed fast food approach. 

    ![site on different devices](static/images/fonts.png)

* Imagery
    Images and the choices of the images is an important component of this site. I chose contemporary, clean images that appeal to the target group. I have four appealing images at the home page to catch the visitors intrerest right away. 

* Icons
    Icons used in footer to set the tone for the sites design approach.(ÄNDRA)

## Wireframes 
* [Mobile](https://github.com/jennymalmoe/MSP3/tree/main/wireframes/mobile###) 
* [Tablet](https://github.com/jennymalmoe/MSP3/tree/main/wireframes/tablet###)
* [Desktop](https://github.com/jennymalmoe/MSP3/tree/main/wireframes/desktop###)

# Features


# Database Design
MongoDB was used for this project and schema design was created. SE MOVIE BILD(ÄNDRA)

# Technologies Used

* Languages, Frameworks and Libraries

* [BSON](https://bsonspec.org/) - bson.objectid is a required dependency for MongoDB management system.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - used to create the styling throughout the site.
* [Google fonts](https://fonts.google.com/) - used to import fonts.
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - used to create the site structure.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - framework used to create and populate the templates.
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - used for the sidenav, back-to-top button, image preview.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Jinja templating language was used to simplify and display backend data in html.
* [jQuery](https://jquery.com/) - used to activate the Materialize functionality.
* [Materialize](https://materializecss.com/) - library used for styling and responsiveness.
* [PyMongo](https://pypi.org/project/pymongo/) - flask_pymongo was used for interacting with MongoDB database from Python.
* [Python](https://www.python.org/) - used to write the logic that operates the site.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - used for password hashing and authentication.
    
    
* Tools and Editors

* [Am I Responsive](http://ami.responsivedesign.is/) - used to validate the responsiveness. 
* [Balsamiq](https://balsamiq.com/) - used to create the wireframes.
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)  - used Lighthouse to check sites performance and the dev tool to check responsiveness.
* [Designwizard](https://www.designwizard.com/) - used for inspirations regarding color combinations.
* [Font-Awesome](https://fontawesome.com/) - used for icons.
* [FreeIcons](https://freeicons.io/) - used for icon in tab.
* [Git](https://git-scm.com/) - used for version control to commit to Git and push to Heroku.
* [GitHub](https://github.com/) - remote repository for application code.
* [Gitpod](https://gitpod.io/) - IDE used for development.
* [Heroku](https://www.heroku.com/home) - cloud platform used to deploy application.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Jinja templating language was used to simplify and display backend data in html.
* [JSHint](https://jshint.com/) - used to test JS code to ensure there were no errors.
* [Unsplash](https://unsplash.com/) - Images used were obtained from Unsplash.
* [PEP8](https://www.python.org/dev/peps/pep-0008/) - Used as style guide for Python code.
* [PEP8online](http://pep8online.com/) - Used to check code for PEP8 requirements
* [Pixelmator](https://www.pixelmator.com/mac/) - used to resize images.
* [Postimages](https://postimages.org/) - used to create url for images. 
* [RandomKeygen](https://randomkeygen.com/) - used to generate secure password to Secret Key. 
* [TechSini](https://techsini.com/) - mockup generator used for preview of the  website.
* [Visual Studio Code](https://code.visualstudio.com/) - IDE used for code editing.
* [W3C Validator](https://validator.w3.org/) - used to test HTML code to ensure there were no errors.
* [W3C Validator CSS](https://validator.w3.org/) - used to test CSS code to ensure there were no errors.

* Database Management
* [MongoDB](https://www.mongodb.com/3) - used for database functionality.
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - used to host the database.

# Testing
Testing information can be found in separate [testing.md file]()

# Deployment
* GitHub Pages
* Forking the GitHub Repository
* Making a Local Clone

# Credits
* Code 
* Content
* Media
* Acknowledgements





