from datetime import date

from fastapi import HTTPException, status

from db_connection import DbConnection


class ToDoArchive:
    def __init__(self):
        self.db = DbConnection()

    def archive_todo(self, todo_id: int, user_id: int):
        try:
            self.db.cursor.execute("""
                INSERT INTO archivetodo 
                (user_id, title, description, category, due_date, status, updated_at, created_at)
                SELECT user_id, title, description, category, due_date, status, updated_at, created_at
                FROM todo WHERE id = %s AND user_id = %s""", (todo_id, user_id))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Error inserting todo into archive table {e}")

        try:
            self.db.cursor.execute("DELETE FROM todo WHERE id = %s AND user_id = %s", (todo_id, user_id))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Error deleting todo {e}")

        try:
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Error committing changes")
