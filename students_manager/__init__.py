from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from students_manager.config import Config
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from students_manager.students import api

    api.init_app(app)

    return app
