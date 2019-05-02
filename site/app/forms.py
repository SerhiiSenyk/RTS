from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class RegisterUserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    id = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Register User')


class RegisterCheckpointForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    id = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Register Checkpoint')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
