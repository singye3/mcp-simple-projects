import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.mark.skip(reason="Requires OAuth setup")
def test_get_notes():
    response = client.get("/api/notes", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 200