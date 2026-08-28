from argon2 import PasswordHasher
from flask import Flask, redirect, render_template, url_for

from app.extensions import csrf, db, login_manager, talisman
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    talisman.init_app(
        app,
        force_https=app.config.get("FORCE_HTTPS", False),
        content_security_policy={"default-src": "'self'"},
    )

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.admin import bp as admin_bp
    from app.auth import bp as auth_bp
    from app.backlogs import bp as backlogs_bp
    from app.criteria import bp as criteria_bp
    from app.epics import bp as epics_bp
    from app.projects import bp as projects_bp
    from app.stories import bp as stories_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(backlogs_bp)
    app.register_blueprint(epics_bp)
    app.register_blueprint(stories_bp)
    app.register_blueprint(criteria_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def index():
        return redirect(url_for("projects.index"))

    @app.errorhandler(403)
    def forbidden(_error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("errors/404.html"), 404

    with app.app_context():
        db.create_all()
        _seed_admin(app)

    return app


def _seed_admin(app):
    from app.models import User

    email = app.config.get("ADMIN_EMAIL")
    password = app.config.get("ADMIN_PASSWORD")
    if not email or not password:
        return

    user = User.query.filter_by(email=email).first()
    if user is None:
        user = User(email=email, password_hash=PasswordHasher().hash(password), role="admin")
        db.session.add(user)
        db.session.commit()
    elif user.role != "admin":
        user.role = "admin"
        db.session.commit()
