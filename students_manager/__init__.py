from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from students_manager.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from students_manager.users.routes import users
    from students_manager.errors.handlers import errors

    app.register_blueprint(errors)
    app.register_blueprint(users)

    return app
