from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from src.app.db import get_db
import bcrypt

bp = Blueprint("auth", __name__)

@bp.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("auth.profile"))
    return redirect(url_for("auth.login"))

@bp.route("/login", methods=["GET", "POST"])
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
            return redirect(url_for("auth.profile"))  # Updated here

        flash("Invalid username or password", "error")
    return render_template("login.html")

@bp.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))  # Updated here
    return render_template("profile.html", photo_url=session.get("photo_url"))

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))  # Updated here

@bp.route('/favicon.ico')
def favicon():
    return '', 204