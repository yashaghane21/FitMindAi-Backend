# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field, ConfigDict

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: str = Field(alias="_id")
    name: str
    email: str

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "60c72b2f9b1d8e25d8f284d7",
                "name": "John Doe",
                "email": "johndoe@example.com"
            }
        }
    )

class Token(BaseModel):
    access_token: str 
    token_type: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
