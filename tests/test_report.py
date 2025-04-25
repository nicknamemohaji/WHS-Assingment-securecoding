from config import *

@pytest.mark.order(4)
def test_report_feature(client):
    login(client, TEST_USERNAME, TEST_PASSWORD)  # Make sure to implement login function or session setup
    resp = client.post('/report/report', data={
        'target': TEST_USERNAME + '2',
        'reason': 'Illegal activity'
    }, follow_redirects=True)
    assert resp.status_code == 200
    assert "Report has been successfully submitted." in resp.text
