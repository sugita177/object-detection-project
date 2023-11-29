from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
import logging

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    csrf = CSRFProtect()

    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=(
            f"sqlite:///{Path(__file__).parent.parent /'local.sqlite'}"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY="AuwzyszU5sugKN7KZs6f",
        DEBUG_TB_INTERCEPT_REDIRECTS=False,
    )

    app.logger.setLevel(logging.DEBUG)

    DebugToolbarExtension(app)

    csrf.init_app(app)

    db.init_app(app)

    Migrate(app, db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    return app
