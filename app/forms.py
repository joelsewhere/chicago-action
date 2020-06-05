from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Email(FlaskForm):
    name = StringField('Name')
    ward = IntegerField('Ward Number', validators=[DataRequired()])

    submit = SubmitField('Create Email')