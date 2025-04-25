from config import *


@pytest.mark.order(6)
def test_item_inspect(client):
    resp = client.get(
        '/items/1'
    )
    assert (resp.status_code == 200
            and b'test1' in resp.data
            and b'test description' in resp.data)
