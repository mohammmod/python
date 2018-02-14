import cs50
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return rander_template("loging.html")

