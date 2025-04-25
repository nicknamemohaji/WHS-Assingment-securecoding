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
    assert (resp.status_code == 200
            and b'Item added successfully' in resp.data
            and b'test1' in resp.data)


@pytest.mark.order(6)
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
                and b'Item added successfully' in resp.data
                and f"__test{i}".encode() in resp.data)

    resp = client.get('/')
    assert '__test1' not in resp.data and '__test6' in resp.data

