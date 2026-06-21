from pydantic import BaseModel,Field


class ProfileUpdate(BaseModel):
    age:int 
    gender: str
    height: float
    goal: str
    activity_level: str
    weight: float


class ProfileResponse(BaseModel):
   id: str 
   name: str 
   email: str 
    
   age: int 
   gender: str 
    
   height: float 
   weight: float 
    
   goal: str 
   activity_level: str 