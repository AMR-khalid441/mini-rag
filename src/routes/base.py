from fastapi import FastAPI , APIRouter
from helpers.config import get_settings
import os
base_router = APIRouter(prefix="/api/v1" , 
                        tags=["api_v1"])


@base_router.get("/")
async def welcome():
    app_settings = get_settings()
    app_name = app_settings.APP_Name
    app_version = app_settings.APP_Version
    return {
        "app_name " : app_name,
        "app_version " : app_version , 
        "welcome": "Hello y'all aaa     !"
    }