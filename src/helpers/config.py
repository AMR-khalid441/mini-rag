from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    APP_Name :str
    APP_Version:str
    OPENAI_API_KEY:str
    class Config:
        env_file = ".env"
def get_settings():
    return Settings()