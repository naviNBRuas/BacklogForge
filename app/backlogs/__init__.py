from flask import Blueprint

bp = Blueprint("backlogs", __name__, url_prefix="/projects/<int:project_id>/backlogs")

from app.backlogs import routes  # noqa: E402,F401
