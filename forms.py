"""script for all form classes"""

from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):

    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
