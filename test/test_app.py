import json
from app.app import app

def test_root():
    client = app.test_client()
    resp = client.get("/")
    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert data.get("message") == "Hello from my-app!"
