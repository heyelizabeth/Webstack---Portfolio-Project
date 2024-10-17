from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_shorten_url():
    response = client.post("/api/shorten", json={"original_url": "https://www.example.com"})
    assert response.status_code == 200
    assert "short_url" in response.json()

def test_redirect_url():
    # First, shorten a URL
    shorten_response = client.post("/api/shorten", json={"original_url": "https://www.example.com"})
    short_url = shorten_response.json()["short_url"]
    
    # Now, attempt to redirect
    redirect_response = client.get(f"/api/{short_url}")
    assert redirect_response.status_code == 200
    assert redirect_response.json()["original_url"] == "https://www.example.com"

def test_list_urls():
    response = client.get("/api/urls")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
