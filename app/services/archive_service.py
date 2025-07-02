from fastapi import APIRouter, HTTPException, status

import main
from db_connection import DbConnection

todo_archive_router = APIRouter(tags=["Todo archive"])


class ToDoArchive:
    def __init__(self):
        self.db = DbConnection()

    def archive_todo(self, todo_id: int):
        try:
            main.cursor.execute("""
                INSERT INTO archivetodo 
                (todo_id, user_id, title, description, category, due_date, status, updated_at, created_at)
                SELECT id, user_id, title, description, category, due_date, status, updated_at, created_at
                FROM todo WHERE id = %s
            """, (todo_id,))
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Error inserting todo into archive table")

        try:
            main.cursor.execute("DELETE FROM todo WHERE id = %s", (todo_id,))
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Error deleting todo")

        try:
            main.conn.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Error committing changes")
