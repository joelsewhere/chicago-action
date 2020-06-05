from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Email(FlaskForm):
    name = StringField('Your Name', render_kw={"placeholder": "Enter your name to populate the email!"})
    ward = IntegerField('Ward Number',
                        render_kw={"placeholder": "Enter a ward number between 1 and 50"}, 
                        validators=[DataRequired()])

    submit = SubmitField('Create Email')

class FindWard(FlaskForm):
    name = StringField('Your name', 
                        render_kw={"placeholder": "Enter your name to populate the email!"})
    address = StringField("Your Address", 
                        render_kw={"placeholder": "Enter your address to find your ward!"},
                        validators=[DataRequired()] )
    submit = SubmitField('Create Email')
