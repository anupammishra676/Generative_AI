import pytest
from fastapi.testclient import TestClient
from app import app, reset_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    reset_db()
    yield
    reset_db()


def test_create_todo():
    response = client.post("/todos/", json={"title": "Buy milk", "description": "2% milk"})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Buy milk"
    assert data["description"] == "2% milk"
    assert data["completed"] is False


def test_list_todos():
    client.post("/todos/", json={"title": "Task 1"})
    client.post("/todos/", json={"title": "Task 2"})

    response = client.get("/todos/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Task 1"
    assert data[1]["title"] == "Task 2"


def test_get_todo_by_id():
    create_resp = client.post("/todos/", json={"title": "Read book"})
    todo_id = create_resp.json()["id"]

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Read book"

    response_404 = client.get("/todos/999")
    assert response_404.status_code == 404


def test_update_todo():
    client.post("/todos/", json={"title": "Initial Title", "description": "Initial Desc"})

    response = client.put("/todos/1", json={"title": "Updated Title", "completed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["description"] == "Initial Desc"
    assert data["completed"] is True

    response_404 = client.put("/todos/999", json={"title": "Doesn't exist"})
    assert response_404.status_code == 404


def test_delete_todo():
    client.post("/todos/", json={"title": "Delete me"})

    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted"

    get_resp = client.get("/todos/1")
    assert get_resp.status_code == 404

    response_404 = client.delete("/todos/999")
    assert response_404.status_code == 404
