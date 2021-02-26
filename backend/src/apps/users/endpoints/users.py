from fastapi import APIRouter

from src.apps.users.fixtures import whale_1, whale_2, whale_3

router = APIRouter()


@router.get("")
def list_users():
    return {"users": [whale_1]}


@router.get("/whales")
def list_whales():
    return {"whales": [whale_1, whale_2, whale_3]}
