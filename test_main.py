
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_students():
    response = client.get("/students/")

    assert response.status_code == 200

def test_invalid_pagination():
    response = client.get("/students/?page=0")

    assert response.status_code == 422

def test_invalid_limit():
    response = client.get("/students/?limit=101")

    assert response.status_code == 422

def test_student_not_found():
    response = client.get("/students/999999")

    assert response.status_code == 404

def test_create_student():
    response = client.post(
        "/students/",
        json={
            "name": "Test User",
            "age": 22,
            "course": "Python"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Test User"

def test_update_student():
    create_response = client.post(
        "/students/",
        json={
            "name": "Original User",
            "age": 22,
            "course": "Python"
        }
    )

    student_id = create_response.json()["id"]

    response = client.put(
        f"/students/{student_id}",
        json={
            "name": "Updated User",
            "age": 23,
            "course": "FastAPI"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"


def test_delete_student():
    create_response = client.post(
        "/students/",
        json={
            "name": "Delete User",
            "age": 22,
            "course": "Python"
        }
    )

    student_id = create_response.json()["id"]

    response = client.delete(f"/students/{student_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Student Deleted Successfully"