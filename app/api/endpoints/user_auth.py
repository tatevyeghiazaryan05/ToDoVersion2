from fastapi import APIRouter, status
from services.user_auth import UserAuth
from schemas.user_auth_schemas import UserSignUpSchema, UserLoginSchema
from schemas.verification_schema import VerificationCodeSchema

user_auth_router = APIRouter()

user_auth_service = UserAuth()


@user_auth_router.post("/api/user/auth/sign-up",
                       status_code=status.HTTP_201_CREATED)
def signup(data: UserSignUpSchema):
    return user_auth_service.signup(data)


@user_auth_router.post("/api/user/auth/verify")
def verify(data: VerificationCodeSchema):
    return user_auth_service.verify(data)


@user_auth_router.post("/api/user/auth/login",
                       status_code=status.HTTP_201_CREATED)
def login(data: UserLoginSchema):
    return user_auth_service.login(data)
