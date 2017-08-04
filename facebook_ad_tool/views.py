from flask import render_template
from flask import flash
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import check_password_hash
from .database import User, session
from flask import request, redirect, url_for
from . import app

@app.route("/")
def home():
    return render_template("base.html")

@login_required
@app.route("/ad-form")
def ad_form():
    return render_template("ad_form.html")
    
@app.route("/login", methods=["GET"])
def login_get():
    if current_user.is_authenticated:
        return redirect(url_for('logged_in'), code=302)
    else:
        return render_template('login.html')

@login_required
@app.route("/loggedin", methods=["GET"])
def logged_in():
    return render_template("loggedin.html", user=current_user)

@login_required
@app.route("/logout", methods=["GET"])
def logout_get():
    logout_user()
    return redirect(url_for('login_get'), code=302)

@app.route("/login", methods=["POST"])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect username or password", "danger")
        return redirect(url_for("login_get"))
    
    login_user(user)
    return redirect(request.args.get('next') or url_for("login_get"))
