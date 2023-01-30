"""script for all form classes"""

from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):

    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
