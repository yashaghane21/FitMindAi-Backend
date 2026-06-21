from bson import ObjectId

async def update_profile(db,user_id:str,profile_data:dict):
    await db.users.update_one(
        {"_id":ObjectId(user_id)},{
            "$set":profile_data
        }
    )

    return await db.users.find_one(
        {"_id":ObjectId(user_id)}
    )