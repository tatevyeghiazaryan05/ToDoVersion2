from fastapi import HTTPException, status

from db_connection import DbConnection
from schemas.user_auth_schemas import UserSignUpSchema
from core.security import pwd_context


class UserAuth:
    def __init__(self):
        self.db = DbConnection()

    def signup(self, data: UserSignUpSchema):
        name = data.name
        email = data.email
        password = data.password
        hashed_password = pwd_context.hash(password)

        try:
            self.db.cursor.execute("""INSERT INTO users 
                                (name,email,password) 
                                VALUES (%s,%s,%s)""",
                                   (name, email, hashed_password))
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def login(self):
        pass
