from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    table_number = IntegerField('Número de Mesa', validators=[DataRequired()])
    submit = SubmitField('Ingresar')


