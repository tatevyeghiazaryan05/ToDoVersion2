from pydantic import BaseModel


class VerificationCodeSchema(BaseModel):
    email: str
    code: str
