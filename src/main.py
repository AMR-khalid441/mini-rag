from fastapi import FastAPI
from helper.config import get_settings
from routes import base , data

app = FastAPI()

# include router
app.include_router(base.base_router)
app.include_router(data.data_router)
