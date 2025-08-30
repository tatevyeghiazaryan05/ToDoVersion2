from pydantic import BaseModel, EmailStr


class UserSignUpSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class VerificationCodeSchema(BaseModel):
    email: str
