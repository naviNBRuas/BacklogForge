from flask import abort, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import audit
from app.criteria import bp
from app.criteria.forms import AcceptanceCriterionForm
from app.extensions import db
from app.models import AcceptanceCriterion, Project, UserStory
from app.security import require_project_owner


@bp.route("/new", methods=["GET", "POST"])
@login_required
def create(project_id, story_id):
    project = _get_project_or_404(project_id)
    story = _get_story_or_404(project, story_id)
    form = AcceptanceCriterionForm()
    if form.validate_on_submit():
        criterion = AcceptanceCriterion(
            user_story_id=story.id,
            given_text=form.given_text.data,
            when_text=form.when_text.data,
            then_text=form.then_text.data,
        )
        db.session.add(criterion)
        db.session.commit()
        audit.log(current_user, "create", "acceptance_criterion", criterion.id)
        return redirect(url_for("stories.detail", project_id=project.id, story_id=story.id))

    return render_template(
        "stories/criterion_form.html", project=project, story=story, form=form, criterion=None
    )


@bp.route("/<int:criterion_id>/edit", methods=["GET", "POST"])
@login_required
def edit(project_id, story_id, criterion_id):
    project = _get_project_or_404(project_id)
    story = _get_story_or_404(project, story_id)
    criterion = _get_criterion_or_404(story, criterion_id)
    form = AcceptanceCriterionForm(obj=criterion)
    if form.validate_on_submit():
        criterion.given_text = form.given_text.data
        criterion.when_text = form.when_text.data
        criterion.then_text = form.then_text.data
        db.session.commit()
        audit.log(current_user, "update", "acceptance_criterion", criterion.id)
        return redirect(url_for("stories.detail", project_id=project.id, story_id=story.id))

    return render_template(
        "stories/criterion_form.html", project=project, story=story, form=form, criterion=criterion
    )


@bp.route("/<int:criterion_id>/delete", methods=["POST"])
@login_required
def delete(project_id, story_id, criterion_id):
    project = _get_project_or_404(project_id)
    story = _get_story_or_404(project, story_id)
    criterion = _get_criterion_or_404(story, criterion_id)
    criterion_id_for_log = criterion.id
    db.session.delete(criterion)
    db.session.commit()
    audit.log(current_user, "delete", "acceptance_criterion", criterion_id_for_log)
    return redirect(url_for("stories.detail", project_id=project.id, story_id=story.id))


def _get_project_or_404(project_id):
    project = Project.query.get(project_id)
    if project is None:
        abort(404)
    require_project_owner(project)
    return project


def _get_story_or_404(project, story_id):
    story = UserStory.query.get(story_id)
    if story is None or story.project.id != project.id:
        abort(404)
    return story


def _get_criterion_or_404(story, criterion_id):
    criterion = AcceptanceCriterion.query.get(criterion_id)
    if criterion is None or criterion.user_story_id != story.id:
        abort(404)
    return criterion
