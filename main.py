"""New website"""
import flask_sqlalchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from forms import LoginForm


def create_app():
    """use Bootsrap"""
    app = Flask(__name__)
    Bootstrap(app)
    return app


frontend = create_app()


@frontend.route("/")
def homepage():
    """welcome page with link to bring you to a login form"""
    return render_template("index.html")


@frontend.route("/login")
def login_page():
    """login form requiring email and password which are sent to database"""
    login = LoginForm()
    return render_template("login.html")


if __name__ == "__main__":
    frontend.run(debug=True)
