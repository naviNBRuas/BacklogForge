from functools import wraps

from flask import abort
from flask_login import current_user


def require_role(role):
    def decorator(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                abort(403)
            return view(*args, **kwargs)

        return wrapped

    return decorator


def require_project_owner(project):
    if not current_user.is_authenticated:
        abort(403)
    if current_user.is_admin:
        return
    if project.owner_id != current_user.id:
        abort(403)
