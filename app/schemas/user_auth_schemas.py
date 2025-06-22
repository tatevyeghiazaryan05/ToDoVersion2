from pydantic import BaseModel,EmailStr


class UserSignUpSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
