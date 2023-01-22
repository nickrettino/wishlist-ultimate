"""New website"""
import flask_sqlalchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


def create_app():
    """use Bootsrap"""
    app = Flask(__name__)
    Bootstrap(app)
    return app


frontend = create_app()


@frontend.route("/")
def homepage():
    return render_template("index.html")


if __name__ == "__main__":
    frontend.run(debug=True)
