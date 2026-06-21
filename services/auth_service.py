import os
from datetime import datetime, timedelta, timezone
# pyrefly: ignore [missing-import]
from fastapi import HTTPException, status
# pyrefly: ignore [missing-import]
import bcrypt
# pyrefly: ignore [missing-import]
import jwt
from schemas.user_schema import UserRegister, UserLogin





def hash_password(password: str) -> str:
    """Hash plain password using bcrypt."""
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify plain password against hashed password."""
    try:
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )

    except Exception:
        return False


async def register_user(db, user: UserRegister) -> dict:
    email_lower = user.email.strip().lower()
    
   
    existing_user = await db.users.find_one({"email": email_lower})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_pwd = hash_password(user.password)
    
    user_dict = {
        "name": user.name.strip(),
        "email": email_lower,
        "password": hashed_pwd,
        "created_at": datetime.now(timezone.utc)
    }
    
    result = await db.users.insert_one(user_dict)

    new_user = await db.users.find_one({"_id": result.inserted_id})
    return new_user



async def authenticate_user(db, credentials: UserLogin) -> dict:

    email_lower = credentials.email.strip().lower()
    
    # Retrieve user from database
    user = await db.users.find_one({"email": email_lower})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Check password
    if not verify_password(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    return user
