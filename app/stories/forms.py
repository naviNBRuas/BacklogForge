from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField
from wtforms.validators import DataRequired, InputRequired, Length, Optional

from app.models import MOSCOW_VALUES, RICE_CONFIDENCE_VALUES, RICE_IMPACT_VALUES, STORY_POINTS_VALUES

STORY_POINTS_CHOICES = [("", "—")] + [(str(v), str(v)) for v in STORY_POINTS_VALUES]
MOSCOW_CHOICES = [("", "—")] + [(v, v) for v in MOSCOW_VALUES]
IMPACT_CHOICES = [("", "—")] + [(str(v), str(v)) for v in RICE_IMPACT_VALUES]
CONFIDENCE_LABELS = {1.0: "100%", 0.8: "80%", 0.5: "50%"}
CONFIDENCE_CHOICES = [("", "—")] + [(str(v), CONFIDENCE_LABELS[v]) for v in RICE_CONFIDENCE_VALUES]


class UserStoryForm(FlaskForm):
    role_text = StringField("As a", validators=[DataRequired(), Length(max=200)])
    action_text = StringField("I want", validators=[DataRequired(), Length(max=300)])
    benefit_text = StringField("So that", validators=[DataRequired(), Length(max=300)])


class StoryEstimateForm(FlaskForm):
    story_points = SelectField("Story points", choices=STORY_POINTS_CHOICES, validators=[Optional()])
    moscow = SelectField("MoSCoW", choices=MOSCOW_CHOICES, validators=[Optional()])
    epic_id = SelectField("Epic", coerce=int, validators=[Optional()])
    rice_reach = FloatField("Reach", validators=[Optional()])
    rice_impact = SelectField("Impact", choices=IMPACT_CHOICES, validators=[Optional()])
    rice_confidence = SelectField("Confidence", choices=CONFIDENCE_CHOICES, validators=[Optional()])
    rice_effort = SelectField("Effort", choices=STORY_POINTS_CHOICES, validators=[Optional()])


class MoveStoryForm(FlaskForm):
    sprint_backlog_id = SelectField("Move to", coerce=int, validators=[InputRequired()])
