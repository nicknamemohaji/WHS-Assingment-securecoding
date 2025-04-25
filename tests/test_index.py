import pytest

from config import client

@pytest.mark.order(1)
def test_index(client):
    response = client.get("/", content_type="html/text")

    assert response.status_code == 200
    assert '로그인'.encode() in response.data
