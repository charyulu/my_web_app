from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from src.app.db import get_db
import bcrypt

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, password_hash, photo_url FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode(), user[1].encode()):
            session["user_id"] = user[0]
            session["photo_url"] = user[2]
            return redirect(url_for("profile"))

        flash("Invalid username or password", "error")
    return render_template("login.html")

@auth.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("profile.html", photo_url=session.get("photo_url"))

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))