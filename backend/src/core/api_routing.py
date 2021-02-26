from fastapi import APIRouter

from src.apps.users.endpoints import users

api_router = APIRouter()


api_router.include_router(users.router, prefix="/users", tags=["users"])
