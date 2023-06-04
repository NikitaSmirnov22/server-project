
# import library
from app import app
from flask import render_template

# add index route
@app.route("/")
def index():
    return render_template("index.html")

# add about route
@app.route("/about")
def about():
    return "<h1 style='color: blue'>ABOUT!</h1>"
