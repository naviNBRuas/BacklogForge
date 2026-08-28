from flask import Blueprint

bp = Blueprint(
    "criteria", __name__, url_prefix="/projects/<int:project_id>/stories/<int:story_id>/criteria"
)

from app.criteria import routes  # noqa: E402,F401
