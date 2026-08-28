from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class AcceptanceCriterionForm(FlaskForm):
    given_text = TextAreaField("Given", validators=[DataRequired()])
    when_text = TextAreaField("When", validators=[DataRequired()])
    then_text = TextAreaField("Then", validators=[DataRequired()])
