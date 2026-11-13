from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Todo App")


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Todo(TodoBase):
    id: int


# In-memory storage
todos_db: dict[int, Todo] = {}
next_id = 1


def reset_db():
    global todos_db, next_id
    todos_db.clear()
    next_id = 1


@app.post("/todos/", response_model=Todo, status_code=status.HTTP_201_CREATED)
@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED, include_in_schema=False)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(
        id=next_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )
    todos_db[next_id] = new_todo
    next_id += 1
    return new_todo


@app.get("/todos/", response_model=List[Todo])
@app.get("/todos", response_model=List[Todo], include_in_schema=False)
def list_todos():
    return list(todos_db.values())


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos_db[todo_id]


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoUpdate):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    stored_todo = todos_db[todo_id]
    update_data = todo_update.model_dump(exclude_unset=True)
    updated_todo = stored_todo.model_copy(update=update_data)
    todos_db[todo_id] = updated_todo
    return updated_todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def delete_todo(todo_id: int):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    deleted = todos_db.pop(todo_id)
    return {"message": "Todo deleted", "id": todo_id}
