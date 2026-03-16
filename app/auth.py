from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
router=APIRouter()
class LoginRequest(BaseModel):
    username:str
    password:str
@router.post("/login")
def login(data:LoginRequest):
    if data.username=="admin"and data.password=="1234":
        return{"message":"login successfully"}
    raise HTTPException(status_code=401,detail="invalid credentials")