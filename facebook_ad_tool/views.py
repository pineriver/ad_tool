from flask import render_template

from . import app

@app.route("/")
def home():
    return render_template("base.html")
    
@app.route("/ad-form")
def ad_form():
    return render_template("ad_form.html")