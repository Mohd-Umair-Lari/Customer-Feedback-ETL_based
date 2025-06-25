import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_and_insights():
    with open("app/sample_products.csv", "rb") as f:
        response = client.post("/upload", files={"file": ("sample_products.csv", f, "text/csv")})
        assert response.status_code == 200
        data = response.json()
        assert "analytics" in data
        assert data["analytics"]["average_price"] == 443.6
        assert data["analytics"]["top_category"] == "Electronics"
        assert round(data["analytics"]["average_rating"], 2) == 4.44

def test_get_insights():
    response = client.get("/insights")
    assert response.status_code == 200
    data = response.json()
    assert "average_price" in data
