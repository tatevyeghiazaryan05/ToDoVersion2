from datetime import datetime

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


