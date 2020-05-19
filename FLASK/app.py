# BASIC FLASK

from flask import Flask # Import the class `Flask` from the `flask` module, written by someone else.

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
    return "Fuck you, world!"

@app.route("/Fuck_off") # when typed in the route "http://127.0.0.1:5000/Fuck_off"
def fuck():
    return "Fuck you all! "

@app.route("/<string:name>") # This takes in the string from url and displays it on the page
def hello(name):
    name = name.capitalize(); # Takes first letter and capitalise it 
    return f"<h1>Hello {name}</h1>" # <h1> is HTML Tag and we can integrate HTML directly to the python 