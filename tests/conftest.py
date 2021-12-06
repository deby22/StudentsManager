import pytest

from flask_sqlalchemy import SQLAlchemy
from students_manager import db, create_app
from students_manager.test_config import TestConfig


@pytest.fixture
def client():
    app = create_app(TestConfig)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.drop_all()
