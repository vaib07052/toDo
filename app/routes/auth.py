from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from werkzeug.security import generate_password_hash, check_password_hash

from app import db

from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user:
            flash("Username already exists", "danger")
            return redirect(url_for("auth.register"))

        hashed = generate_password_hash(password)

        new_user = User(
            username=username,
            password=hashed
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):

            session["user"] = user.id

            flash("Login Successful", "success")

            return redirect(url_for("tasks.view_tasks"))

        flash("Invalid Username or Password", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():

    session.clear()

    flash("Logged Out", "info")

    return redirect(url_for("auth.login"))