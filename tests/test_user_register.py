from config import *

@pytest.mark.order(2)
def test_register(client):
    # test register
    with client:
        resp = register(client, TEST_USERNAME, TEST_PASSWORD, TEST_DESCRIPTION)
        assert resp.status_code == 200 and b'Registration successful!' in resp.data
        # dummy data
        register(client, TEST_USERNAME+'2', TEST_PASSWORD, TEST_DESCRIPTION + '__')
    # test duplicate check
    with client:
        resp = register(client, TEST_USERNAME, TEST_PASSWORD, TEST_DESCRIPTION)
        assert b'Registration successful!' not in resp.data


@pytest.mark.order(3)
def test_login(client):
    resp = login(client, TEST_USERNAME, TEST_PASSWORD)
    assert resp.status_code == 200 and b'Login successful' in resp.data
    resp = client.get('/')
    assert f"Hello {TEST_USERNAME}!".encode() in resp.data

    client.delete_cookie('session')
    resp = login(client, TEST_USERNAME, 'notcorrect')
    assert  resp.status_code == 200 and b'Invalid username or password' in resp.data

@pytest.mark.order(3)
def test_logout(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    resp = logout(client)
    assert resp.status_code == 200 and b'Logout successful' in resp.data

