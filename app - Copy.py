from flask import Flask, redirect, url_for, render_template, request, session
import datetime
import sys
import os




app = Flask(__name__)



@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        user =request.form["nm"]

        session["user"] = user
        return redirect(url_for("home"))
    else:
        return render_template("login.html")


@app.route("/")
def film():
    
    return render_template("film.html")
                           



@app.route("/home")
def home():      
        return render_template("index.html")
  



if __name__== "__main__":
    app.run(debug=True)