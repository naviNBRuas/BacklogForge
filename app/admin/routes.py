from flask import render_template, request
from flask_login import login_required

from app.admin import bp
from app.models import AuditLog, Project, User
from app.security import require_role


@bp.route("/")
@login_required
@require_role("admin")
def dashboard():
    return render_template(
        "admin/dashboard.html",
        user_count=User.query.count(),
        project_count=Project.query.count(),
    )


@bp.route("/users")
@login_required
@require_role("admin")
def users():
    return render_template("admin/users.html", users=User.query.order_by(User.created_at).all())


@bp.route("/projects")
@login_required
@require_role("admin")
def projects():
    return render_template(
        "admin/projects.html", projects=Project.query.order_by(Project.created_at).all()
    )


@bp.route("/audit-logs")
@login_required
@require_role("admin")
def audit_logs():
    query = AuditLog.query
    user_id = request.args.get("user_id", type=int)
    action = request.args.get("action", type=str)
    if user_id:
        query = query.filter(AuditLog.actor_id == user_id)
    if action:
        query = query.filter(AuditLog.action == action)

    logs = query.order_by(AuditLog.created_at.desc()).all()
    return render_template(
        "admin/audit_logs.html", logs=logs, users=User.query.all(), selected_user_id=user_id,
        selected_action=action,
    )
