from fastapi.testclient import TestClient
from todo import app  # Import your FastAPI app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the To-Do List API!"}

def test_create_todo():
    # Create a new to-do item
    response = client.post("/todos/", json={"id": 1, "title": "First task", "description": "This is the first task"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "First task",
        "description": "This is the first task",
        "completed": False
    }

def test_get_all_todos():
    # Get all to-do items
    response = client.get("/todos/")
    assert response.status_code == 200
    # Check if the to-do list contains the created to-do item
    assert response.json() == [
        {
            "id": 1,
            "title": "First task",
            "description": "This is the first task",
            "completed": False
        }
    ]

def test_get_todo_by_id():
    # Get a specific to-do item by ID
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "First task",
        "description": "This is the first task",
        "completed": False
    }

def test_update_todo():
    # Update the to-do item
    response = client.put("/todos/1", json={
        "id": 1,
        "title": "Updated task",
        "description": "This is the updated task",
        "completed": True
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Updated task",
        "description": "This is the updated task",
        "completed": True
    }

def test_delete_todo():
    # Delete the to-do item
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"message": "To-Do item deleted"}

    # Ensure the item no longer exists
    response = client.get("/todos/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "To-Do item not found"}
