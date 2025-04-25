from config import *


@pytest.mark.order(10)
def test_item_inspect(client):
    resp = client.get(
        '/items/5'
    )
    print(resp.data, resp.request.url)
    assert resp.status_code == 200
    assert '커피'.encode() in resp.data
    assert b'test description' in resp.data
