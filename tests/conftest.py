import pytest
from src.app import app as create_app
from src.db import db
@pytest.fixture(scope="session")
def app():
    """Instance of Main flask app"""
    return create_app

@pytest.fixture
def client():
    app_conf = create_app
    app_conf.config["TESTING"] = True
    app_conf.testing = True
    client = app_conf.test_client()
    with app_conf.app_context():
        db.create_all()
    yield client
