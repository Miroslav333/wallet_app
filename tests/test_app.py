from fastapi.testclient import TestClient
from app import api


client = TestClient(api)


def test_show_wallet_balance():
    response = client.get('/v1/wallets/32d71f67-d058-4c76-a8a6-ee6ddec41369')
    assert response.status_code == 200


def test_deposit_operation():
    operation = {"operation": "DEPOSIT", "amount": 500}
    response = client.post('/v1/wallets/32d71f67-d058-4c76-a8a6-ee6ddec41369/operation', json=operation)
    assert response.status_code == 200


def test_withdraw_operation():
    operation = {"operation": "WITHDRAW", "amount": 300}
    response = client.post('/v1/wallets/32d71f67-d058-4c76-a8a6-ee6ddec41369/operation', json=operation)
    assert response.status_code == 200

