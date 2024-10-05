from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

class ToDoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

app = FastAPI()

# In-memory storage for to-do items (for demo purposes)
todo_list = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do List API!"}

@app.post("/todos/", response_model=ToDoItem)
def create_todo(todo: ToDoItem):
    todo_list.append(todo)
    return todo

@app.get("/todos/", response_model=list[ToDoItem])
def get_all_todos():
    return todo_list

@app.get("/todos/{todo_id}", response_model=ToDoItem)
def get_todo_by_id(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="To-Do item not found")

@app.put("/todos/{todo_id}", response_model=ToDoItem)
def update_todo(todo_id: int, updated_todo: ToDoItem):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="To-Do item not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "To-Do item deleted"}
    raise HTTPException(status_code=404, detail="To-Do item not found")


# --- Tests Section ---
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the To-Do List API!"}

def test_create_todo():
    new_todo = {
        "id": 1,
        "title": "Test ToDo",
        "description": "This is a test to-do item",
        "completed": False
    }
    response = client.post("/todos/", json=new_todo)
    assert response.status_code == 200
    assert response.json() == new_todo

def test_get_all_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) > 0
    assert todos[0]["title"] == "Test ToDo"

def test_get_todo_by_id():
    response = client.get("/todos/1")
    assert response.status_code == 200
    todo = response.json()
    assert todo["id"] == 1
    assert todo["title"] == "Test ToDo"

def test_update_todo():
    updated_todo = {
        "id": 1,
        "title": "Updated ToDo",
        "description": "Updated description",
        "completed": True
    }
    response = client.put("/todos/1", json=updated_todo)
    assert response.status_code == 200
    assert response.json() == updated_todo

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"message": "To-Do item deleted"}

    # Verify it's deleted by trying to get the same to-do item
    response = client.get("/todos/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "To-Do item not found"}

# This block ensures tests are only run if you execute the script directly

test_read_root()
test_create_todo()
test_get_all_todos()
test_get_todo_by_id()
test_update_todo()
test_delete_todo()
print("All tests passed!")
