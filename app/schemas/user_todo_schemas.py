from datetime import date

from pydantic import BaseModel


class ToDoCreateSchema(BaseModel):
    title: str
    description: str
    category: str
    due_date: date
