"""
Model for the web form on the home page.
"""

from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    """ Simple form """
    name = StringField('Name', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    doubler = FloatField('Doubler', validators=[DataRequired()])
    vehicle = StringField('Vehicle', validators=[DataRequired()], default='Bronco')

