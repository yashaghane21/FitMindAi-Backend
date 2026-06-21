
# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, status

from schemas.user_schema import (
    UserRegister,
    UserLogin,
    UserResponse,
    LoginResponse,
)

from database.db import get_database
from services.auth_service import (
    register_user,
    authenticate_user,
)
from core.security import create_access_token
from core.dependencies import get_current_user
router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)

async def register(user: UserRegister, db = Depends(get_database)):
    new_user = await register_user(db, user)
    return new_user




@router.post("/login", response_model=LoginResponse)
async def login(credentials: UserLogin, db=Depends(get_database)):

    user = await authenticate_user(db, credentials)

    user["_id"] = str(user["_id"])

    access_token = create_access_token(
        data={
            "sub": user["email"],
            "user_id": user["_id"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }

@router.get("/me")
async def get_me(
    current_user=Depends(get_current_user)
):
    return current_user