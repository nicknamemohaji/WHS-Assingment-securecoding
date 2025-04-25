from config import *

@pytest.mark.order(9)
def test_my_items_manage_page(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    resp = client.get('/items/mine')
    assert resp.status_code == 200
    assert '커피_9'.encode() in resp.data


@pytest.mark.order(9)
def test_my_items_hide(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    resp = client.post(
        '/items/mine/1',
        data={
            'visible': 'False'
        },
        follow_redirects=True
    )
    assert resp.status_code == 200
    assert 'Item 1(노트북) is hidden' in resp.text

    resp = client.get('/items/1')
    assert resp.status_code == 404

    resp = client.post(
        '/items/mine/1',
        data={
            'visible': 'True'
        },
        follow_redirects=True
    )
    assert resp.status_code == 200
    assert 'Item 1(노트북) is visible'.encode() in resp.data

    resp = client.get('/items/1')
    assert resp.status_code == 200

