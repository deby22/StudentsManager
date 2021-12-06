import os
import tempfile

import pytest

from flask_sqlalchemy import SQLAlchemy
from students_manager import create_app
db = SQLAlchemy()

@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
        yield client
