from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app import audit
from app.auth import bp
from app.auth.forms import LoginForm, SignupForm
from app.extensions import db
from app.models import User

hasher = PasswordHasher()
# A valid Argon2 hash with no matching plaintext, verified when the email
# isn't found, so lookup and login-failure paths take comparable time and
# response timing can't be used to enumerate registered emails.
DUMMY_HASH = PasswordHasher().hash("not-a-real-password")


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("projects.index"))

    form = SignupForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("An account with this email already exists.", "danger")
            return render_template("auth/signup.html", form=form)

        user = User(
            email=form.email.data,
            password_hash=hasher.hash(form.password.data),
        )
        db.session.add(user)
        db.session.commit()
        audit.log(user, "signup", "user", user.id)
        flash("Account created. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/signup.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("projects.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # Always call _check_password, even with no matching user, so the
        # unknown-email and wrong-password paths take comparable time.
        password_ok = _check_password(user, form.password.data)
        if user and password_ok:
            login_user(user)
            audit.log(user, "login", "user", user.id)
            return redirect(url_for("projects.index"))

        audit.log(None, "login_failed", "user", None)
        flash("Invalid email or password.", "danger")

    return render_template("auth/login.html", form=form)


@bp.route("/logout", methods=["POST"])
@login_required
def logout():
    audit.log(current_user, "logout", "user", current_user.id)
    logout_user()
    return redirect(url_for("auth.login"))


def _check_password(user, password):
    stored_hash = user.password_hash if user else DUMMY_HASH
    try:
        return hasher.verify(stored_hash, password)
    except VerifyMismatchError:
        return False
