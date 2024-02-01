from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fetch_drivers():
    response = client.get("/fetch_drivers?startDate=2020-01-03&endDate=2021-12-27&minScore=3.0&maxScore=4.0&limit=50&offset=0")
    data = response.json()
    assert response.status_code == 200
    assert data["msg"] == "Success"
