import pytest

from students_manager import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        # with app.app_context():
        #     init_db()
        yield client