from fastapi import APIRouter, status
from services.user_todo_crud import ToDoCRUD
from schemas.user_todo_schemas import ToDoCreateSchema

todo_crud_router = APIRouter()

todo_crud_service = ToDoCRUD()


@todo_crud_router.post("/api/todo/add/todo",
                       status_code=status.HTTP_201_CREATED)
def create_todo(data: ToDoCreateSchema):
    return todo_crud_service.todo_create(data)
