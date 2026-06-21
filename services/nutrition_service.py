
TRAINING_MULTIPLIERS = {
    0: 1.20,
    1: 1.30,
    2: 1.40,
    3: 1.50,
    4: 1.55,
    5: 1.60,
    6: 1.60,
    7: 1.65
}

GOALS = {
    "fat_loss": -500,
    "muscle_gain": 250
}

def calculate_bmr(
    weight: float,
    height: float,
    age: int,
    gender: str
) -> float:

    gender = gender.lower()

    if gender == "male":
        bmr = (
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            + 5
        )
    else:
        bmr = (
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            - 161
        )

    return round(bmr)




def calculate_tdee(
    bmr: float,
    training_days_per_week: int
) -> float:

    multiplier = TRAINING_MULTIPLIERS.get(
        training_days_per_week,
        1.20
    )

    return round(bmr * multiplier)




def calculate_target_calories(
    tdee: float,
    goal: str
) -> float:

    adjustment = GOALS.get(goal.lower(), 0)

    return round(tdee + adjustment)



def calculate_macros(
    weight: float,
    target_calories: float,
    goal: str
) -> dict:

    goal = goal.lower()

    if goal == "fat_loss":

        protein = weight * 2.2
        fat = weight * 0.8

    else:  # muscle_gain

        protein = weight * 2.0
        fat = weight * 1.0

    protein_calories = protein * 4
    fat_calories = fat * 9

    remaining_calories = (
        target_calories
        - protein_calories
        - fat_calories
    )

    carbs = remaining_calories / 4

    return {
        "protein": round(protein),
        "carbs": round(carbs),
        "fat": round(fat)
    }




def calculate_timeline(
    current_weight: float,
    target_weight: float,
    goal: str
) -> dict:

    weight_difference = abs(
        target_weight - current_weight
    )

    if goal == "fat_loss":
        weekly_change = 0.5
    else:
        weekly_change = 0.25

    weeks = max(
        1,
        round(weight_difference / weekly_change)
    )

    return {
        "weekly_weight_change": weekly_change,
        "estimated_weeks": weeks
    }