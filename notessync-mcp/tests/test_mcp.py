import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_mcp_inspector():
    response = client.get("/mcp/inspector")
    assert response.status_code == 200