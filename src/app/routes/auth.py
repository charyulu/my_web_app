from flask import Blueprint, render_template, redirect, url_for, request

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Dummy login logic
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "user" and password == "pass":
            return redirect(url_for("auth.profile"))
        return "Invalid credentials", 401
    return render_template("login.html")

@auth_bp.route("/profile")
def profile():
    return render_template("profile.html", photo_url="static/images/photo.jpg")