from fastapi import APIRouter
from schemas.user_schema import UserRegister



router=APIRouter();

@router.post("/register")
def register(user:UserRegister):
    return {
       "message": "User Registered",
        "user": user
    }