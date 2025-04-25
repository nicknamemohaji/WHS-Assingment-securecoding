# from config import *
#
#
# @pytest.mark.order(2)
# def test_chat_room_list(client):
#     resp = client.get('/chat/all')
#     assert resp.status_code == 200
#     assert b'전체 채팅' in resp.data
#
#
# @pytest.mark.order(2)
# def test_private_chat_room(client):
#     resp = client.get('/chat/with/user123')
#     assert resp.status_code == 200
#     assert b'1대1 채팅' in resp.data
#
# ----
#
# import pytest

# ---
# import pytest
#
# @pytest.mark.order(5)
# def test_transfer_instruction_page(client):
#     resp = client.get('/transfer/with/user123')
#     assert resp.status_code == 200
#     assert b'계좌번호' in resp.data
#     assert b'송금 금액' in resp.data
#
# @pytest.mark.order(6)
# def test_transfer_result_page(client):
#     resp = client.get('/transfer/result/user123')
#     assert resp.status_code == 200
#     assert b'송금 완료' in resp.data or b'입금 확인' in resp.data
#
# ----
# import pytest
#
# @pytest.mark.order(9)
# def test_admin_report_list(client):
#     resp = client.get('/admin/reports')
#     assert resp.status_code == 200
#     assert b'신고 목록' in resp.data
#     assert b'삭제' in resp.data or b'차단' in resp.data
#
# @pytest.mark.order(10)
# def test_admin_item_manage(client):
#     resp = client.get('/admin/items')
#     assert resp.status_code == 200
#     assert b'상품 관리' in resp.data
#     assert b'수정' in resp.data or b'삭제' in resp.data
