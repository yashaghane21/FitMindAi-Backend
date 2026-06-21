from fastapi import APIRouter, Depends
from bson import ObjectId

from database.db import get_database
from core.dependencies import get_current_user

from services.nutrition_service import (
    calculate_bmr,
    calculate_tdee,
    calculate_target_calories,
    calculate_macros
)

router = APIRouter(
    prefix="/nutrition"
)


@router.get("/targets")
async def get_nutrition_targets(
    current_user=Depends(get_current_user),
    db=Depends(get_database)
):

    user_id = current_user["user_id"]

    user = await db.users.find_one(
        {"_id": ObjectId(user_id)}
    )

    if not user:
        return {
            "message": "User not found"
        }

    bmr = calculate_bmr(
        weight=user["weight"],
        height=user["height"],
        age=user["age"],
        gender=user["gender"]
    )

    print("USER =>", user)

    tdee = calculate_tdee(
    bmr=bmr,
    training_days_per_week=user["training_days_per_week"]
)

    target_calories = calculate_target_calories(
        tdee=tdee,
        goal=user["goal"]
    )
    
    macros = calculate_macros(
        weight=user["weight"],
        target_calories=target_calories,
        goal=user["goal"]
    )
    
    return {
        "bmr": round(bmr),
        "tdee": round(tdee),
        "target_calories": round(target_calories),
        **macros
    }