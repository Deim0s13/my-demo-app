import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app
from extensions import db
from models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing

    with app.app_context():
        db.create_all()  # Create tables for all models
        yield app.test_client()
        db.session.remove()
        db.drop_all()  # Drop all tables after the test

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_register_route(client):
    response = client.post('/register', data=dict(username="testuser", email="test@example.com"), follow_redirects=True)
    assert response.status_code == 200

    # Check that the response contains the username or email, which indicates a successful registration
    assert b"testuser" in response.data
    assert b"test@example.com" in response.data