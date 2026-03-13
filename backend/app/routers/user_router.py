from fastapi import APIRouter
from backend.app.auth.auth_handler import create_token
router=APIRouter()
@router.get("/login")
def login():
    token=create_token({"user":"john","role":"doctor"})
    return{"token":token}