from flask import Blueprint

bp = Blueprint("epics", __name__, url_prefix="/projects/<int:project_id>/epics")

from app.epics import routes  # noqa: E402,F401
