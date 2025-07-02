from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status

from core.security import get_current_user
from services.todo_filters import ToDoFilters

todo_filters_router = APIRouter(tags=["Todo filters"])

todo_filters_service = ToDoFilters()


@todo_filters_router.get("/all/unfinished/todo")
def get_unfinished_todo(token=Depends(get_current_user)):

    try:
        user_id = token.get("id")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Token error")

    return todo_filters_service.get_unfinished_todo(user_id)


@todo_filters_router.get("/by/title/{title}")
def get_todo_by_title(title: str,
                      token=Depends(get_current_user)):

    try:
        user_id = token.get("id")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Token error")

    return todo_filters_service.get_todo_by_title(user_id, title)


@todo_filters_router.get("/all/by/category/{category}")
def get_todo_by_category(category: str,
                         token=Depends(get_current_user)):

    try:
        user_id = token.get("id")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Token error")

    return todo_filters_service.get_todo_by_category(category, user_id)


@todo_filters_router.get("/all/by/due_date/{start_date}/{end_date}")
def get_todo_by_due_date(start_date: date,
                         end_date: date,
                         token=Depends(get_current_user)):

    try:
        user_id = token.get("id")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Token error")

    return todo_filters_service.get_todo_by_due_date(start_date, end_date, user_id)
