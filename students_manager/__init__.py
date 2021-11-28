from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from students_manager.config import Config
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from students_manager.students.routes import students
    from students_manager.errors.handlers import errors

    app.register_blueprint(errors)
    app.register_blueprint(students)

    return app
