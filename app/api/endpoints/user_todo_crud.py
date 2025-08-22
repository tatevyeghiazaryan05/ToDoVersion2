import os
print(os.getcwd())
from fastapi import APIRouter, status, Depends, HTTPException
from core.security import get_current_user
from services.user_todo_crud import ToDoCRUD
from schemas.todo_crud_schemas import ToDoCreateSchema, TodoUpdateSchema

todo_crud_router = APIRouter(tags=["Todo CRUD"])

todo_crud_service = ToDoCRUD()


@todo_crud_router.post("/ToDo/api/todo/add/todo",
                       status_code=status.HTTP_201_CREATED)
def create_todo(data: ToDoCreateSchema,
                token=Depends(get_current_user)):

    try:
        user_id = token.get("id")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Token fetch error"
            )

    return todo_crud_service.todo_create(data, user_id)


@todo_crud_router.put("/ToDo/api/todo/change/{todo_id}")
def change_todo(todo_id: int,
                data: TodoUpdateSchema,
                token=Depends(get_current_user)):
    return todo_crud_service.update_todo(data, todo_id)


@todo_crud_router.delete("/ToDo/api/todo/delete/todo/{todo_id}")
def delete_todo(todo_id: int):
    return todo_crud_service.delete_todo(todo_id)


@todo_crud_router.get("/ToDo/api/todo/get/all/todo")
def get_todo(token=Depends(get_current_user)):
    try:
        user_id = token.get("id")
        print(user_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Token fetch error"
            )
    return todo_crud_service.get_all_todos(user_id)


@todo_crud_router.get("/ToDo/api/todo/get/todo/{todo_id}")
def get_todo(todo_id: int, token=Depends(get_current_user)):
    return todo_crud_service.get_todo(todo_id)
