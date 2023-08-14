from fastapi import APIRouter, HTTPException, Depends
from model.auth import UserLoginRequest, UserRegistrationRequest
from schema.auth import user_serializer, users_serializer
import uvicorn
from core.config import user_db 
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from routers.jwt_handler import get_access_token
from fastapi.encoders import jsonable_encoder

authRouter = APIRouter()

@authRouter.get("/users/whoami", tags = ["users"])
async def viewMe():
    return current_user;

@authRouter.post("/login", tags=["users"])
async def login(userIn: OAuth2PasswordRequestForm = Depends()):
    user = user_db.find_one({
        "user_name": userIn.username,
        "pass_word": userIn.password
    })
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = get_access_token(userIn.username)
    token = jsonable_encoder(access_token)
    content = {
        "message": "You've successfully logged in. Welcome back!",
        "user": userIn.username,
        "token": access_token
        }
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=600,
        samesite="Lax",
        secure=False,
    )

    return response
# async def login(user: UserLoginRequest):
#     user = user_db.find_one({
#         "user_name": user.user_name,
#         "pass_word": user.pass_word
#     })
#     if(user):
#         return {
#             "status": "Login successfully",
#             "data": user_serializer(user)
#         }
#     else:
#         raise HTTPException(
#             status_code=404, detail="Login failed, pls check you username and password"
#         )
    
@authRouter.post("/register",  tags=["users"])
async def register(user_registration: UserRegistrationRequest):
    user =  user_db.find_one({
        "user_name": user_registration.user_name
    })
    if(user):
        return {
            "msg": "User name is existed",
            "data": None
        }
    _id = user_db.insert_one(dict(user_registration))
    user = user_serializer(user_db.find_one({"_id": _id.inserted_id}))
    return {
        "msg": "Register Successfully",
        "data": user
    }  


