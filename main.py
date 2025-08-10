from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome():
    return {
        "welcome": "Hello y'all !"
    }