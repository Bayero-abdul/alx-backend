#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Flask Babel Configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale() -> str:
    """Gets the local language.
    """
    return request.accept_languages.best_match(
        app.config.get('LANGUAGES', ['en', 'fr']))


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Handles root route.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
