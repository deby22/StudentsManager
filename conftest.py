import pytest

from students_manager import create_app
from students_manager.test_config import TestConfig


@pytest.fixture
def client():
    app = create_app()

    with app.test_client(TestConfig) as client:
        # with app.app_context():
        #     init_db()
        yield client
