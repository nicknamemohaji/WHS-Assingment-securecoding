from config import *


@pytest.mark.order(8)
def test_item_search(client):
    resp = client.get('/items/search?query=커피')
    assert resp.status_code == 200
    assert '커피_1' in resp.text

    resp = client.get('/items/search?query=에너지드링크')
    assert resp.status_code == 200
    assert '결과 없음' in resp.text

    resp = client.get('/items/search?query=커피_0')
    assert resp.status_code == 200
    print(resp.text)
    assert '커피_0' in resp.text
