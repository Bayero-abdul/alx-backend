#!/usr/bin/env python3
"""2-app.py """


from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """App Configuration. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """Gets the local language. """
    return request.accept_languages.best_match(
        app.config.get('LANGUAGES', ['en', 'fr']))


app.config.from_object(Config)


@app.route("/")
def index():
    """Handles root route. """
    return render_template('2-index.html', lang=get_locale()), 200


if __name__ == "__main__":
    app.run()
