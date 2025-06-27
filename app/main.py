from fastapi import FastAPI

from api.endpoints import user_auth, user_todo_crud
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_auth.user_auth_router)
app.include_router(user_todo_crud.todo_crud_router)
