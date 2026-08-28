from flask import abort, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import audit
from app.epics import bp
from app.epics.forms import EpicForm
from app.extensions import db
from app.models import Epic, Project
from app.security import require_project_owner


@bp.route("/")
@login_required
def index(project_id):
    project = _get_project_or_404(project_id)
    return render_template("epics/index.html", project=project)


@bp.route("/new", methods=["GET", "POST"])
@login_required
def create(project_id):
    project = _get_project_or_404(project_id)
    form = EpicForm()
    if form.validate_on_submit():
        epic = Epic(project_id=project.id, name=form.name.data, description=form.description.data)
        db.session.add(epic)
        db.session.commit()
        audit.log(current_user, "create", "epic", epic.id)
        return redirect(url_for("epics.detail", project_id=project.id, epic_id=epic.id))

    return render_template("epics/form.html", project=project, form=form, epic=None)


@bp.route("/<int:epic_id>")
@login_required
def detail(project_id, epic_id):
    project = _get_project_or_404(project_id)
    epic = _get_epic_or_404(project, epic_id)
    return render_template("epics/detail.html", project=project, epic=epic)


@bp.route("/<int:epic_id>/edit", methods=["GET", "POST"])
@login_required
def edit(project_id, epic_id):
    project = _get_project_or_404(project_id)
    epic = _get_epic_or_404(project, epic_id)
    form = EpicForm(obj=epic)
    if form.validate_on_submit():
        epic.name = form.name.data
        epic.description = form.description.data
        db.session.commit()
        audit.log(current_user, "update", "epic", epic.id)
        return redirect(url_for("epics.detail", project_id=project.id, epic_id=epic.id))

    return render_template("epics/form.html", project=project, form=form, epic=epic)


@bp.route("/<int:epic_id>/delete", methods=["POST"])
@login_required
def delete(project_id, epic_id):
    project = _get_project_or_404(project_id)
    epic = _get_epic_or_404(project, epic_id)
    for story in list(epic.stories):
        story.epic_id = None
    epic_id_for_log = epic.id
    db.session.delete(epic)
    db.session.commit()
    audit.log(current_user, "delete", "epic", epic_id_for_log)
    return redirect(url_for("epics.index", project_id=project.id))


def _get_project_or_404(project_id):
    project = Project.query.get(project_id)
    if project is None:
        abort(404)
    require_project_owner(project)
    return project


def _get_epic_or_404(project, epic_id):
    epic = Epic.query.get(epic_id)
    if epic is None or epic.project_id != project.id:
        abort(404)
    return epic
