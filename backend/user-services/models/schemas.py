from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
# import uuid


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    # model_config = ConfigDict(
    #     from_attributes=True,
    #     json_encoders={uuid.UUID: lambda v: str(v)}
    # )


class Token(BaseModel):
    access_token: str

class UserWithToken(UserOut):
    access_token: str
