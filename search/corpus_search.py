import sys
# sys.path.insert(0, '.../')
# sys.path.insert(0, '.../app/')

from web_app import app as application, get_locale as app_get_locale
from flask_babel import Babel
from flask import Flask

babel = Babel(application)


@babel.localeselector
def get_locale():
    return app_get_locale()

app = Flask(__name__)

if __name__ == "__main__":
    application.run(port=7342, host='0.0.0.0',
                    debug=False, use_reloader=False)
