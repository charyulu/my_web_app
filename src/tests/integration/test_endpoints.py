import pytest
from flask import Flask
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data  # Check if "Login" text is in the page

def test_profile_page_requires_login(client):
    response = client.get("/profile")
    assert response.status_code == 302  # Redirect to login page for unauthenticated users
    assert "/login" in response.headers["Location"]