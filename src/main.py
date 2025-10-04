from fastapi import FastAPI
from helper.config import get_settings
from routes import base

app = FastAPI()

# include router
app.include_router(base.base_router)
