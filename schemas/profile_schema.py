from pydantic import BaseModel,Field


class ProfileUpdate(BaseModel):
    age: int
    gender: str
    height: float
    weight: float

    goal: str

    training_days_per_week: int

class ProfileResponse(BaseModel):
   id: str 
   name: str 
   email: str 
    
   age: int 
   gender: str 
    
   height: float 
   weight: float 
    
   goal: str 
   training_days_per_week: int 