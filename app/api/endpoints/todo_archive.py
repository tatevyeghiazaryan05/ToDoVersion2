from fastapi import APIRouter, status, Depends, HTTPException
from core.security import get_current_user
from services.user_todo_crud import ToDoCRUD


todo_archive_router = APIRouter(tags=["Todo archive"])

todo_crud_service = ToDoCRUD()


@todo_archive_router.get("/api/todo/archive/{todo_id}",
                         status_code=status.HTTP_201_CREATED)
def archive_todo(todo_id: int,
                 token=Depends(get_current_user)):

    try:
        user_id = token.get("id")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Token fetch error"
            )

    return todo_crud_service.todo_create(todo_id, user_id)
