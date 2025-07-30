# test_api.py
import pytest
from app import app, db, Transaction

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        db.session.query(Transaction).delete()
        db.session.commit()
    with app.test_client() as client:
        yield client

def test_valid_sum(client):
    resp = client.post("/api/sum", json={"numbers": [1, 2, 3]})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data["sum"] == 6
    assert data["cached"] is False
    
    # Repeat request should be cached
    resp2 = client.post("/api/sum", json={"numbers": [3, 2, 1]})
    data2 = resp2.get_json()
    assert resp2.status_code == 200
    assert data2["sum"] == 6
    assert data2["cached"] is True

def test_missing_field(client):
    resp = client.post("/api/sum", json={})
    assert resp.status_code == 400

def test_non_number_list(client):
    resp = client.post("/api/sum", json={"numbers": "abc"})
    assert resp.status_code == 400

    resp2 = client.post("/api/sum", json={"numbers": [1, "x", 3]})
    assert resp2.status_code == 400
