import os

import pytest

from project.app import app

@pytest.fixture
def client():
    DB_NAME = '/db_test.sqlite3'
    DB_PATH = '../project/instance' + DB_NAME
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + DB_NAME
    yield app.test_client() # tests run here


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
        }
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