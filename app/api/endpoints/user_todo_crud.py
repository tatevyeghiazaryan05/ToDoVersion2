import os
print(os.getcwd())
from fastapi import APIRouter, status, Depends, HTTPException
from core.security import get_current_user
from services.user_todo_crud import ToDoCRUD
from schemas.user_todo_schemas import ToDoCreateSchema

todo_crud_router = APIRouter()

todo_crud_service = ToDoCRUD()


@todo_crud_router.post("/api/todo/add/todo",
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
