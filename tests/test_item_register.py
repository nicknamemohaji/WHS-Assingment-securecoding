from pathlib import Path

from config import *

IMAGE = Path(__file__).parent / "resources"


@pytest.mark.order(5)
def test_item_register(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    resp = client.post(
        '/items/register',
        data={
            'name': 'test1',
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
    assert (resp.status_code == 200
            and b'test1' in resp.data)


@pytest.mark.order(7)
def test_item_register_bulk(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)
    for i in range(10):
        resp = client.post(
            '/items/register',
            data={
                'name': f"__test{i}",
                'price': i,
                'description': 'test description',
                'image': (IMAGE / "test.png").open("rb")
            },
            follow_redirects=True
        )
        assert (resp.status_code == 200
                and b'Item added successfully')

    resp = client.get('/items/recents')
    assert b'__test1' not in resp.data and b'__test6' in resp.data

