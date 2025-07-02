from fastapi import APIRouter, status, Depends, HTTPException
from core.security import get_current_user
from services.archive_service import ToDoArchive

todo_archive_router = APIRouter(tags=["Todo archive"])

todo_archive_service = ToDoArchive()


@todo_archive_router.post("/api/todo/archive/{todo_id}",
                          status_code=status.HTTP_201_CREATED)
def archive_todo(todo_id: int,
                 token=Depends(get_current_user)):
    try:
        user_id = token.get("id")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Token error")

    return todo_archive_service.archive_todo(todo_id, user_id)
