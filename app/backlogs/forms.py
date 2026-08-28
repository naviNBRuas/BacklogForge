from flask_wtf import FlaskForm
from wtforms import DateField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class ProductBacklogForm(FlaskForm):
    notes = TextAreaField("Notes")


class SprintBacklogForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=200)])
    start_date = DateField("Start date", validators=[Optional()])
    end_date = DateField("End date", validators=[Optional()])
