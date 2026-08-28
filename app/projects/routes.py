from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import audit
from app.extensions import db
from app.models import Project, ProductBacklog
from app.projects import bp
from app.projects.forms import ProjectForm
from app.security import require_project_owner


@bp.route("/")
@login_required
def index():
    projects = Project.query.filter_by(owner_id=current_user.id).all()
    return render_template("projects/index.html", projects=projects)


@bp.route("/new", methods=["GET", "POST"])
@login_required
def create():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            owner_id=current_user.id,
        )
        db.session.add(project)
        db.session.flush()
        db.session.add(ProductBacklog(project_id=project.id))
        db.session.commit()
        audit.log(current_user, "create", "project", project.id)
        return redirect(url_for("projects.detail", project_id=project.id))

    return render_template("projects/form.html", form=form, project=None)


@bp.route("/<int:project_id>")
@login_required
def detail(project_id):
    project = _get_project_or_404(project_id)
    return render_template("projects/detail.html", project=project)


@bp.route("/<int:project_id>/edit", methods=["GET", "POST"])
@login_required
def edit(project_id):
    project = _get_project_or_404(project_id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        db.session.commit()
        audit.log(current_user, "update", "project", project.id)
        return redirect(url_for("projects.detail", project_id=project.id))

    return render_template("projects/form.html", form=form, project=project)


@bp.route("/<int:project_id>/delete", methods=["POST"])
@login_required
def delete(project_id):
    project = _get_project_or_404(project_id)
    project_id_for_log = project.id
    db.session.delete(project)
    db.session.commit()
    audit.log(current_user, "delete", "project", project_id_for_log)
    flash("Project deleted.", "success")
    return redirect(url_for("projects.index"))


def _get_project_or_404(project_id):
    project = Project.query.get(project_id)
    if project is None:
        abort(404)
    require_project_owner(project)
    return project
