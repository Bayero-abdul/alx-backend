#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""


from flask import Flask, render_template, request, g, session
from flask_babel import Babel, Locale


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    lang = request.args.get('locale', None)
    if lang:
        return Locale(language=lang)
    return request.accept_languages.best_match(
        app.config.get('LANGUAGES', ['en', 'fr']))


def get_user() -> dict:
    """Finds a user.
    """
    user_id = request.args.get('login_as', None)
    if user_id:
        return users.get(int(user_id), None)
    return None


@app.before_request
def before_request() -> None:
    """Gets a user before each request.
    """
    g.user = get_user()


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Handles root route.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
