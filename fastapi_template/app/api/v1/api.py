from fastapi import APIRouter

from app.api.v1.endpoints import login, accounts

api_router = APIRouter()

api_router.include_router(login.router, prefix="/login", tags=["Login"])
api_router.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])