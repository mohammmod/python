from flask import Flask,render_template,request
#from datetime import datetime
#from pytz import timezone

app = Flask(__name__)

@app.route("/")
def time():
    name = request.form.get("bro")
   # return (print(name))
    return render_template("index.html")

@app.route("/emoji.py", methods=["POST"])
def emoji():
    return render_template("emoji.html")

