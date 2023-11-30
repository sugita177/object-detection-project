from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
from apps.config import config
import logging

db = SQLAlchemy()


def create_app(config_key):
    app = Flask(__name__)

    csrf = CSRFProtect()

    app.config.from_object(config[config_key])

    app.logger.setLevel(logging.DEBUG)

    DebugToolbarExtension(app)

    csrf.init_app(app)

    db.init_app(app)

    Migrate(app, db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    return app
