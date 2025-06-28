from datetime import date

from pydantic import BaseModel
from typing import Optional


class ToDoCreateSchema(BaseModel):
    title: str
    description: str
    category: str
    due_date: date


class TodoUpdateSchema(BaseModel):
    todo_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[str] = None
