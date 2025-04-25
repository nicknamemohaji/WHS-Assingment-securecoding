from pathlib import Path
import json

from config import *

IMAGE = Path(__file__).parent / "resources"


@pytest.mark.order(5)
def test_item_register(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    resp = client.post(
        '/items/register',
        data={
            'name': '노트북',
            'price': 100,
            'description': 'test description',
            'image': (IMAGE / "test.png").open("rb")
        },
        follow_redirects=True
    )
    assert b'Item registered successfully' in resp.data
    resp = client.get(
        '/items/recents'
    )
    assert resp.status_code == 200
    assert '노트북' == json.loads(resp.text)[-1]['name']



@pytest.mark.order(7)
def test_item_register_bulk(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    for i in range(10):
        resp = client.post(
            '/items/register',
            data={
                'name': f"커피_{i}",
                'price': i + 10,
                'description': 'test description',
                'image': (IMAGE / "test.png").open("rb")
            },
            follow_redirects=True
        )
        assert resp.status_code == 200
        assert b'Item registered successfully' in resp.data

    resp = client.get('/items/recents')
    assert '커피_1' not in [d['name'] for d in json.loads(resp.text)]
    assert '커피_6' in [d['name'] for d in json.loads(resp.text)]
