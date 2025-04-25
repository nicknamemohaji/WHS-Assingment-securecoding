import pytest

from project.app import app

@pytest.fixture
def client():
    yield app.test_client()


TEST_USERNAME = "testuser"
TEST_PASSWORD = "testuser"
TEST_DESCRIPTION = "test description"

def register(client, username, password, description):
    return client.post(
        '/users/register',
        data={
            'username': username,
            'password': password,
            'description': description
        },
        follow_redirects=True
    )

def login(client, username, password):
    return client.post(
        '/users/login',
        data={
            'username': username,
            'password': password
        },
        follow_redirects=True
    )

def logout(client):
    return client.get(
        '/users/logout',
        follow_redirects=True
    )