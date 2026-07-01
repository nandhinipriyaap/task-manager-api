from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

client.post(
    "/register",
    json={
        "username": "testuser",
        "password": "test123"
    }
)

login_response = client.post(
    "/login",
    json={
        "username": "testuser",
        "password": "test123"
    }
)

token = login_response.json()["access_token"]

headers = {
    "Authorization": f"Bearer {token}"
}

def test_get_tasks():
    response = client.get("/tasks", headers=headers)
    assert response.status_code == 200

def test_create_task():
    response = client.post(
        "/tasks",
        headers=headers,
        json={
            "title": "Test Task",
            "completed": False
        }
    )

    assert response.status_code == 201    

def test_delete_task():
    response = client.delete("/tasks/1", headers=headers)

    assert response.status_code in [200, 404]
def test_update_task():
    response = client.put(
        "/tasks/1",
        headers=headers,
        json={
            "title": "Updated Task",
            "completed": True
        }
    )

    assert response.status_code in [200, 404]
def test_create_and_delete_task():
    create_response = client.post(
        "/tasks",
        headers=headers,
        json={
            "title": "Temporary Task",
            "completed": False
        }
    )

    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}", headers=headers)

    assert delete_response.status_code == 200