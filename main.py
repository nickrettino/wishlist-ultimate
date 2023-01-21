"""New website"""
import flask_sqlalchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


def create_app():
    """use Bootsrap"""
    app = Flask(__name__)
    Bootstrap(app)

    @app.route("/")
    def home_page():
        """this is the route for the homepage of the website"""

        return render_template("index.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
