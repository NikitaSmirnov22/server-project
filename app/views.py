
# import library
from app import app

# add index route
@app.route("/")
def index():
    return "Hello world!"

# add about route
@app.route("/about")
def about():
    return "<h1 style='color: blue'>ABOUT!</h1>"
