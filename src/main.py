from fastapi import FastAPI
from dotenv import load_dotenv
from routes import base  # assuming your routes/base.py exists

load_dotenv(".env")  # load environment variables

app = FastAPI()

# include router
app.include_router(base.base_router)
