import pytest
from flask import session
from src.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data

def test_login_valid_user(client):
    with client:
        response = client.post("/login", data={"username": "test_user", "password": "your_password_here"})
        assert response.status_code == 302  # Redirect to profile
        assert session["user_id"] is not None

def test_login_invalid_user(client):
    response = client.post("/login", data={"username": "invalid", "password": "wrong"})
    assert b"Invalid username or password" in response.data