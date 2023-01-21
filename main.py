"""New website"""

import flask
import flask_bootstrap
import flask_sqlalchemy

app = Flask(__name__)


@app.route("/")
def home_page():
    return "<p> Hello, World!</p>"
