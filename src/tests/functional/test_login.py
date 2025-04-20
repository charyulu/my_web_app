import pytest
from flask import Flask
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post("/login", data={"username": "user", "password": "pass"})
    assert response.status_code == 302  # Redirect to profile page
    assert "/profile" in response.headers["Location"]

def test_login_failure(client):
    response = client.post("/login", data={"username": "wrong_user", "password": "wrong_pass"})
    assert response.status_code == 401  # Unauthorized
    assert b"Invalid credentials" in response.data