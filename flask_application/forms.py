from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class CustomRequestForm(FlaskForm):
    subject_1 = StringField("Subject 1", validators=[DataRequired()])
    subject_2 = StringField("Subject 2")
    place = StringField("Place", validators=[DataRequired()])
    action = StringField("Action", validators=[DataRequired()])
    quantity = IntegerField("How much creatives do you want? (Divided by 4)")
    submit = SubmitField("Submit")

