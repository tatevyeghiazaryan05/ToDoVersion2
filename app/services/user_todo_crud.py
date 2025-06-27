from fastapi import HTTPException, status
from fastapi import Depends

from core.security import get_current_user

from db_connection import DbConnection
from schemas.user_todo_schemas import ToDoCreateSchema


class ToDoCRUD:
    def __init__(self):
        self.db = DbConnection()

    def todo_create(self, data: ToDoCreateSchema, user_id: int):
        title = data.title
        category = data.category
        description = data.description
        due_date = data.due_date

        try:
            self.db.cursor.execute(
                """INSERT INTO todo (user_id, category, title, description, due_date)
                 VALUES (%s, %s, %s, %s, %s)""",
                (user_id, category, title, description, due_date)
            )
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=500, detail="Server error during todo addition")
