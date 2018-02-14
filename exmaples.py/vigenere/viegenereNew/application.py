from flask import Flask,request, render_template,flash
#from get import new_scanner
#from preparator import Perparator
from cipher import Cipher

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def time():
    if request.method == "POST":

        key = request.form.get("key")
        plainText = request.form.get("plainText")

        if not key :
            return render_template("index.html")
        if not plainText:
            return render_template("index.html")
        if ' ' in key:
             return render_template("index.html")
        cipher_guy = Cipher()
    #    if len(key)!= 2:
     #       return render_template("index.html")


        ciphertext = cipher_guy.cipher(plainText,key)

        return  ciphertext

       # Cipherguy().doingAlgorithem(plainText,key)

    return render_template("index.html")


