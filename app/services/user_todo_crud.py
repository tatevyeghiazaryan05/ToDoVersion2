from datetime import datetime

from fastapi import HTTPException, status
from fastapi import Depends

from core.security import get_current_user

from db_connection import DbConnection
from schemas.todo_crud_schemas import ToDoCreateSchema, TodoUpdateSchema


class ToDoCRUD:
    def __init__(self):
        self.db = DbConnection()

    def todo_create(self,
                    data: ToDoCreateSchema,
                    user_id: int):

        title = data.title
        category = data.category
        description = data.description
        due_date = data.due_date

        try:
            self.db.cursor.execute(
                """INSERT INTO todo (user_id, category, title, description, due_date, status, archived)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (user_id, category, title, description, due_date, False, False)
            )
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=500, detail="Server error during todo addition")

    def update_todo(self,
                    updates: TodoUpdateSchema,
                    todo_id: int):
        try:
            self.db.cursor.execute("""SELECT * FROM todo WHERE id=%s""", (todo_id,))
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database query error")

        try:
            todo = self.db.cursor.fetchone()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database fetch error")

        if todo is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found!"
            )

        try:
            todo = dict(todo)
            update_data = updates.model_dump()

            for key, value in update_data.items():
                if value is None:
                    setattr(updates, key, todo[key])

            updated_at = datetime.now()

            self.db.cursor.execute("""UPDATE todo SET 
                                    title=%s, description=%s, category=%s, 
                                    status=%s, due_date=%s, updated_at=%s
                                    WHERE id=%s""",
                                   (updates.title, updates.description,
                                    updates.category, updates.status,
                                    updates.due_date, updated_at, todo_id))
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error updating todo")

    def delete_todo(self,
                    todo_id: int):

        try:
            self.db.cursor.execute("DELETE FROM todo WHERE id=%s",
                                   (todo_id,))
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=500, detail="Server error during todo deletion")

    def get_all_todos(self,
                      user_id: int):
        try:
            self.db.cursor.execute("SELECT * FROM todo where user_id=%s",
                                   (user_id,))
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database query error")

        try:
            todos = self.db.cursor.fetchall()

        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database fetch error")

        return todos
