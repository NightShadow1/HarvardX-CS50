from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Pera","Zika","Mika","Kure"] #List of names 
    return render_template("index.html",names=names) # we send those names to index.html 