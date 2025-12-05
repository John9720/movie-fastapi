from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from user_jwt import createToken

login_user=APIRouter()

class User(BaseModel):
    email: str
    password: str

@login_user.post("/login", tags=["Authentication"])
def login(user: User):
    if user.email == 'string@outlook.com' and user.password == 'string123':
        token: str = createToken(user.model_dump())
        return JSONResponse(content=token)