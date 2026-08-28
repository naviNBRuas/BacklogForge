from app.extensions import db
from app.models import AuditLog


def log(actor, action, entity_type=None, entity_id=None):
    entry = AuditLog(
        actor_id=actor.id if actor and getattr(actor, "is_authenticated", False) else None,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
    )
    db.session.add(entry)
    db.session.commit()
    return entry
