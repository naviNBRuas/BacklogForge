from flask import Blueprint

bp = Blueprint("stories", __name__, url_prefix="/projects/<int:project_id>")

from app.stories import routes  # noqa: E402,F401
