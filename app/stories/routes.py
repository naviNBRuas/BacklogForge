from flask import abort, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import audit
from app.extensions import db
from app.models import Project, UserStory
from app.security import require_project_owner
from app.stories import bp
from app.stories.forms import MoveStoryForm, StoryEstimateForm, UserStoryForm


@bp.route("/product/stories/new", methods=["GET", "POST"])
@login_required
def create(project_id):
    project = _get_project_or_404(project_id)
    form = UserStoryForm()
    if form.validate_on_submit():
        story = UserStory(
            product_backlog_id=project.product_backlog.id,
            role_text=form.role_text.data,
            action_text=form.action_text.data,
            benefit_text=form.benefit_text.data,
        )
        db.session.add(story)
        db.session.commit()
        audit.log(current_user, "create", "user_story", story.id)
        return redirect(url_for("stories.detail", project_id=project.id, story_id=story.id))

    return render_template("stories/form.html", project=project, form=form, story=None)


@bp.route("/stories/<int:story_id>")
@login_required
def detail(project_id, story_id):
    project = _get_project_or_404(project_id)
    story = _get_story_or_404(project, story_id)
    estimate_form = _build_estimate_form(project, story)
    move_form = _build_move_form(project)
    move_form.sprint_backlog_id.data = story.sprint_backlog_id or 0
    return render_template(
        "stories/detail.html",
        project=project,
        story=story,
        estimate_form=estimate_form,
        move_form=move_form,
    )


@bp.route("/stories/<int:story_id>/edit", methods=["GET", "POST"])
@login_required
def edit(project_id, story_id):
    project = _get_project_or_404(project_id)
    story = _get_story_or_404(project, story_id)
    form = UserStoryForm(obj=story)
    if form.validate_on_submit():
        story.role_text = form.role_text.data
        story.action_text = form.action_text.data
        story.benefit_text = form.benefit_text.data
        db.session.commit()
        audit.log(current_user, "update", "user_story", story.id)
        return redirect(url_for("stories.detail", project_id=project.id, story_id=story.id))

    return render_template("stories/form.html", project=project, form=form, story=story)


@bp.route("/stories/<int:story_id>/estimate", methods=["POST"])
@login_required
def estimate(project_id, story_id):
    project = _get_project_or_404(project_id)
    story = _get_story_or_404(project, story_id)
    form = _build_estimate_form(project, story)
    if form.validate_on_submit():
        story.story_points = int(form.story_points.data) if form.story_points.data else None
        story.moscow = form.moscow.data or None
        story.epic_id = form.epic_id.data or None
        story.rice_reach = form.rice_reach.data
        story.rice_impact = float(form.rice_impact.data) if form.rice_impact.data else None
        story.rice_confidence = (
            float(form.rice_confidence.data) if form.rice_confidence.data else None
        )
        story.rice_effort = int(form.rice_effort.data) if form.rice_effort.data else None
        db.session.commit()
        audit.log(current_user, "update", "user_story", story.id)

    return redirect(url_for("stories.detail", project_id=project.id, story_id=story.id))


@bp.route("/stories/<int:story_id>/move", methods=["POST"])
@login_required
def move(project_id, story_id):
    project = _get_project_or_404(project_id)
    story = _get_story_or_404(project, story_id)
    form = _build_move_form(project)
    if form.validate_on_submit():
        destination = form.sprint_backlog_id.data
        if destination == 0:
            story.sprint_backlog_id = None
            story.product_backlog_id = project.product_backlog.id
        else:
            story.product_backlog_id = None
            story.sprint_backlog_id = destination
        db.session.commit()
        audit.log(current_user, "update", "user_story", story.id)

    return redirect(url_for("stories.detail", project_id=project.id, story_id=story.id))


@bp.route("/stories/<int:story_id>/delete", methods=["POST"])
@login_required
def delete(project_id, story_id):
    project = _get_project_or_404(project_id)
    story = _get_story_or_404(project, story_id)
    story_id_for_log = story.id
    db.session.delete(story)
    db.session.commit()
    audit.log(current_user, "delete", "user_story", story_id_for_log)
    return redirect(url_for("backlogs.product", project_id=project.id))


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


def _build_estimate_form(project, story):
    form = StoryEstimateForm(obj=story)
    form.epic_id.choices = [(0, "(none)")] + [(e.id, e.name) for e in project.epics]
    if not form.is_submitted():
        form.epic_id.data = story.epic_id or 0
        form.story_points.data = str(story.story_points) if story.story_points is not None else ""
        form.rice_impact.data = str(story.rice_impact) if story.rice_impact is not None else ""
        form.rice_confidence.data = (
            str(story.rice_confidence) if story.rice_confidence is not None else ""
        )
        form.rice_effort.data = str(story.rice_effort) if story.rice_effort is not None else ""
    return form


def _build_move_form(project):
    form = MoveStoryForm()
    form.sprint_backlog_id.choices = [(0, "Product Backlog")] + [
        (s.id, s.name) for s in project.sprint_backlogs
    ]
    return form
