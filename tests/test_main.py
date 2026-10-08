from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_items():
    response = client.get("/api/items")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item():
    response = client.get("/api/items/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_create_item():
    response = client.post(
        "/api/items",
        json={
            "name": "Test item",
            "description": "Created in test"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Test item"


def test_update_item():
    response = client.put(
        "/api/items/1",
        json={
            "name": "Updated item",
            "description": "Updated in test"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated item"


def test_delete_item():
    response = client.delete("/api/items/2")

    assert response.status_code == 204


def test_get_missing_item():
    response = client.get("/api/items/99999")

    assert response.status_code == 404