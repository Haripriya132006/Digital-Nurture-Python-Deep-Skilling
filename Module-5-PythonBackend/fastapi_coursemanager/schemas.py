from pydantic import BaseModel,EmailStr
from typing import Optional,List
from datetime import date






class UserCreate(BaseModel):
          email:EmailStr
          password:str 

class UserResponse(BaseModel):
          id:int
          email:EmailStr
          is_active:bool
          
          class Config:
                    from_attributes=True
class TokenResponse(BaseModel):
          access_token: str
          token_type: str