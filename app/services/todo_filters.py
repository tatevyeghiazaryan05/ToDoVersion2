from datetime import date

from fastapi import HTTPException, status
from fastapi import Depends

from core.security import get_current_user

from db_connection import DbConnection


class ToDoFilters:
    def __init__(self):
        self.db = DbConnection()

    def get_unfinished_todo(self,
                            user_id: int):
        try:
            self.db.cursor.execute("""SELECT * FROM todo where 
                                   user_id = %s AND status=%s""",
                                   (user_id, False))
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database query error")

        try:
            todos = self.db.cursor.fetchall()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database fetch error")

        return todos

    def get_todo_by_title(self, user_id: int, title: str):
        try:
            self.db.cursor.execute("SELECT * FROM todo where user_id = %s AND title=%s",
                                   (user_id, title))
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database query error")

        try:
            todo = self.db.cursor.fetchone()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database fetch error")

        if todo is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No ToDo found in this date range")
        return todo

    def get_todo_by_category(self, category: str, user_id: int):
        try:
            self.db.cursor.execute("SELECT * FROM todo where user_id = %s AND category=%s",
                                   (user_id, category))
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database query error")

        try:
            todos = self.db.cursor.fetchall()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database fetch error")

        return todos

    def get_todo_by_due_date(self, start_date: date, end_date: date, user_id: int):
        try:
            self.db.cursor.execute("SELECT * FROM todo where "
                                   "user_id = %s AND deadline>=%s AND deadline<=%s",
                                   (user_id, start_date, end_date))
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database query error")

        try:
            todos = self.db.cursor.fetchall()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database fetch error")
        return todos
