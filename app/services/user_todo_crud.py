from fastapi import HTTPException, status

from db_connection import DbConnection
from schemas.user_todo_schemas import ToDoCreateSchema


class ToDoCRUD:
    def __init__(self):
        self.db = DbConnection()

    def todo_create(self, data: ToDoCreateSchema):
        return "Created"
