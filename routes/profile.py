from fastapi import APIRouter, Depends
from bson import ObjectId
from database.db import get_database

from schemas.profile_schema import (
    ProfileUpdate,
    ProfileResponse
)

from core.dependencies import get_current_user
router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("/")
async def get_profile(
    current_user=Depends(get_current_user),
    db=Depends(get_database)
):
    print(current_user)
    print(type(current_user["user_id"]))
    user_id = current_user["user_id"]

    user = await db.users.find_one(
        {"_id": ObjectId(user_id)}
    )

    if user:
        user["_id"] = str(user["_id"])

    return user


@router.put("/")
async def update_profile(
    profile: ProfileUpdate,
    current_user=Depends(get_current_user),
    db=Depends(get_database)
):

    user_id = current_user["user_id"]

    await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "age": profile.age,
                "gender": profile.gender,
                "height": profile.height,
                "weight": profile.weight,
                "goal": profile.goal,
                "training_days_per_week": profile.training_days_per_week
            }
        }
    )

    user = await db.users.find_one(
        {"_id": ObjectId(user_id)}
    )

    if user:
        user["_id"] = str(user["_id"])

    return user