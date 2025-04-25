from config import *

@pytest.mark.order(4)
def test_mypage_mine(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    resp = client.get(
        f"/users/mypage/{TEST_USERNAME}"
    )
    assert (resp.status_code == 200
            and TEST_DESCRIPTION.encode() in resp.data
            and b'Edit' in resp.data)


@pytest.mark.order(5)
def test_mypage_other(client):
    resp = client.get(
        f"/users/mypage/{TEST_USERNAME + '2'}"
    )
    assert (resp.status_code == 200
            and (TEST_DESCRIPTION + '__').encode() in resp.data
            and b'Edit' not in resp.data)


@pytest.mark.order(5)
def test_mypage_update(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    resp = client.post(
        f"/users/mypage/{TEST_USERNAME}",
        data={
            'description': TEST_DESCRIPTION[::-1]
        },
        follow_redirects=True
    )
    assert (resp.status_code == 200 and b'Successfully updated.' in resp.data)
    resp = client.get(
        f"/users/mypage/{TEST_USERNAME}"
    )
    assert TEST_DESCRIPTION[::-1].encode() in resp.data

    resp = client.post(
        f"/users/mypage/{TEST_USERNAME}",
        data={
            'description': TEST_DESCRIPTION,
            'PASSWORD': TEST_PASSWORD
        },
        follow_redirects=True
    )
    assert (resp.status_code == 200 and b'Successfully updated.' in resp.data)

    resp = login(client, TEST_USERNAME, TEST_PASSWORD)
    assert resp.status_code == 200 and  b'Login successful' in resp.data

    client.post(
        f"/users/mypage/{TEST_USERNAME}",
        data={
            'description': TEST_DESCRIPTION,
            'PASSWORD': TEST_PASSWORD
        }
    )




