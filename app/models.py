from datetime import datetime

from flask_login import UserMixin

from app.extensions import db

STORY_POINTS_VALUES = (0, 1, 2, 3, 5, 8, 13, 21, 34, 55)
MOSCOW_VALUES = ("M", "S", "C", "W")
RICE_IMPACT_VALUES = (3, 2, 1, 0.5, 0.25)
RICE_CONFIDENCE_VALUES = (1.0, 0.8, 0.5)
ROLE_VALUES = ("user", "admin")


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="user")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    projects = db.relationship(
        "Project", backref="owner", cascade="all, delete-orphan"
    )

    @property
    def is_admin(self):
        return self.role == "admin"


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    product_backlog = db.relationship(
        "ProductBacklog", backref="project", uselist=False,
        cascade="all, delete-orphan",
    )
    sprint_backlogs = db.relationship(
        "SprintBacklog", backref="project", cascade="all, delete-orphan"
    )
    epics = db.relationship("Epic", backref="project", cascade="all, delete-orphan")


class ProductBacklog(db.Model):
    __tablename__ = "product_backlogs"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(
        db.Integer, db.ForeignKey("projects.id"), unique=True, nullable=False
    )
    notes = db.Column(db.Text)

    stories = db.relationship("UserStory", backref="product_backlog")


class SprintBacklog(db.Model):
    __tablename__ = "sprint_backlogs"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    stories = db.relationship("UserStory", backref="sprint_backlog")


class Epic(db.Model):
    __tablename__ = "epics"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    stories = db.relationship("UserStory", backref="epic")


class UserStory(db.Model):
    __tablename__ = "user_stories"

    id = db.Column(db.Integer, primary_key=True)
    product_backlog_id = db.Column(db.Integer, db.ForeignKey("product_backlogs.id"))
    sprint_backlog_id = db.Column(db.Integer, db.ForeignKey("sprint_backlogs.id"))
    epic_id = db.Column(db.Integer, db.ForeignKey("epics.id"))

    role_text = db.Column(db.String(200), nullable=False)
    action_text = db.Column(db.String(300), nullable=False)
    benefit_text = db.Column(db.String(300), nullable=False)

    story_points = db.Column(db.Integer)
    moscow = db.Column(db.String(1))
    rice_reach = db.Column(db.Float)
    rice_impact = db.Column(db.Float)
    rice_confidence = db.Column(db.Float)
    rice_effort = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    acceptance_criteria = db.relationship(
        "AcceptanceCriterion", backref="user_story", cascade="all, delete-orphan"
    )

    @property
    def project(self):
        if self.product_backlog_id:
            return self.product_backlog.project
        return self.sprint_backlog.project

    @property
    def rice_score(self):
        if None in (self.rice_reach, self.rice_impact, self.rice_confidence, self.rice_effort):
            return None
        if self.rice_effort == 0:
            return None
        return (self.rice_reach * self.rice_impact * self.rice_confidence) / self.rice_effort

    def __repr__(self):
        return f"As a {self.role_text} I want {self.action_text} so that {self.benefit_text}"


class AcceptanceCriterion(db.Model):
    __tablename__ = "acceptance_criteria"

    id = db.Column(db.Integer, primary_key=True)
    user_story_id = db.Column(
        db.Integer, db.ForeignKey("user_stories.id"), nullable=False
    )
    given_text = db.Column(db.Text, nullable=False)
    when_text = db.Column(db.Text, nullable=False)
    then_text = db.Column(db.Text, nullable=False)


class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    action = db.Column(db.String(50), nullable=False)
    entity_type = db.Column(db.String(50))
    entity_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    actor = db.relationship("User")
