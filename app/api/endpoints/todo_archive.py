from fastapi import APIRouter, status, Depends
from core.security import get_current_user
from services.archive_service import ToDoArchive


todo_archive_router = APIRouter(tags=["Todo archive"])

todo_archive_service = ToDoArchive()


@todo_archive_router.get("/api/todo/archive/{todo_id}",
                         status_code=status.HTTP_201_CREATED)
def archive_todo(todo_id: int,
                 token=Depends(get_current_user)):

    return todo_archive_service.todo_archive(todo_id)
