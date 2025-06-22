from fastapi import FastAPI

from api.endpoints import user_auth, user_todo_crud


app = FastAPI()

app.include_router(user_auth.user_auth_router)
app.include_router(user_todo_crud.todo_crud_router)
