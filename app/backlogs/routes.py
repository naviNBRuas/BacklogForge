from flask import abort, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import audit
from app.backlogs import bp
from app.backlogs.forms import ProductBacklogForm, SprintBacklogForm
from app.extensions import db
from app.models import Project, SprintBacklog
from app.security import require_project_owner


@bp.route("/product", methods=["GET", "POST"])
@login_required
def product(project_id):
    project = _get_project_or_404(project_id)
    backlog = project.product_backlog
    form = ProductBacklogForm(obj=backlog)
    if form.validate_on_submit():
        backlog.notes = form.notes.data
        db.session.commit()
        audit.log(current_user, "update", "product_backlog", backlog.id)
        return redirect(url_for("backlogs.product", project_id=project.id))

    return render_template(
        "backlogs/product.html", project=project, backlog=backlog, form=form
    )


@bp.route("/sprints/new", methods=["GET", "POST"])
@login_required
def create_sprint(project_id):
    project = _get_project_or_404(project_id)
    form = SprintBacklogForm()
    if form.validate_on_submit():
        sprint = SprintBacklog(
            project_id=project.id,
            name=form.name.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
        )
        db.session.add(sprint)
        db.session.commit()
        audit.log(current_user, "create", "sprint_backlog", sprint.id)
        return redirect(url_for("backlogs.sprint_detail", project_id=project.id, sprint_id=sprint.id))

    return render_template("backlogs/sprint_form.html", project=project, form=form, sprint=None)


@bp.route("/sprints/<int:sprint_id>")
@login_required
def sprint_detail(project_id, sprint_id):
    project = _get_project_or_404(project_id)
    sprint = _get_sprint_or_404(project, sprint_id)
    return render_template("backlogs/sprint_detail.html", project=project, sprint=sprint)


@bp.route("/sprints/<int:sprint_id>/edit", methods=["GET", "POST"])
@login_required
def edit_sprint(project_id, sprint_id):
    project = _get_project_or_404(project_id)
    sprint = _get_sprint_or_404(project, sprint_id)
    form = SprintBacklogForm(obj=sprint)
    if form.validate_on_submit():
        sprint.name = form.name.data
        sprint.start_date = form.start_date.data
        sprint.end_date = form.end_date.data
        db.session.commit()
        audit.log(current_user, "update", "sprint_backlog", sprint.id)
        return redirect(url_for("backlogs.sprint_detail", project_id=project.id, sprint_id=sprint.id))

    return render_template("backlogs/sprint_form.html", project=project, form=form, sprint=sprint)


@bp.route("/sprints/<int:sprint_id>/delete", methods=["POST"])
@login_required
def delete_sprint(project_id, sprint_id):
    project = _get_project_or_404(project_id)
    sprint = _get_sprint_or_404(project, sprint_id)
    for story in list(sprint.stories):
        story.sprint_backlog_id = None
        story.product_backlog_id = project.product_backlog.id
    sprint_id_for_log = sprint.id
    db.session.delete(sprint)
    db.session.commit()
    audit.log(current_user, "delete", "sprint_backlog", sprint_id_for_log)
    return redirect(url_for("projects.detail", project_id=project.id))


def _get_project_or_404(project_id):
    project = Project.query.get(project_id)
    if project is None:
        abort(404)
    require_project_owner(project)
    return project


def _get_sprint_or_404(project, sprint_id):
    sprint = SprintBacklog.query.get(sprint_id)
    if sprint is None or sprint.project_id != project.id:
        abort(404)
    return sprint
