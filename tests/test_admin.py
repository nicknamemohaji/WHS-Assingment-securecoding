from config import *
import pytest

@pytest.mark.order(5)
def test_admin_reports(client):
    # Test unresolved reports
    resp = client.get('/admin/reports/')
    assert resp.status_code == 200
    assert 'Unresolved Reports: 1' in resp.text

    # Test resolving a report
    resp = client.post('/admin/reports/1/act', data={'action': 'ban_user'}, follow_redirects=True)
    assert resp.status_code == 200
    assert 'User has been banned' in resp.text

    # Test resolved reports
    resp = client.get('/admin/reports/resolved')
    assert resp.status_code == 200
    assert 'Resolved Reports: 1' in resp.text

@pytest.mark.order(6)
def test_admin_items(client):
    # Test listing all items including hidden ones
    resp = client.get('/admin/items/list')
    assert resp.status_code == 200
    assert 'Item List' in resp.text

    # Test hiding/showing specific item
    resp = client.post('/admin/items/1', data={'visible': 'False'}, follow_redirects=True)
    assert resp.status_code == 200
    assert 'Item 1 (노트북) is now hidden' in resp.text

@pytest.mark.order(7)
def test_admin_users(client):
    # Test listing all users including banned ones
    resp = client.get('/admin/users/list')
    assert resp.status_code == 200
    assert 'User List' in resp.text

    # Test banning/unbanning user
    resp = client.post('/admin/users/' + TEST_USERNAME + '2', data={'action': 'ban'}, follow_redirects=True)
    assert resp.status_code == 200
    assert TEST_USERNAME + '2 has been banned' in resp.text
