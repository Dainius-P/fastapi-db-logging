from fastapi.testclient import TestClient
from app.database import fastapi_logs, db
from app.main import app


client = TestClient(app)

def test_get():
    response = client.get("/get_test/?name=Test")
    assert response.status_code == 200
    assert response.json() == {"hello": "Test"}

def test_post():
    response = client.post("/post_test/", json={"name": "Test"})
    assert response.status_code == 200
    assert response.json() == {"hello": "Test"}