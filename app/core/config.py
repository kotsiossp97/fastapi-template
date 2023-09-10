from pydantic import BaseSettings
import secrets

class Settings(BaseSettings):
    AUTHOR: str = "Awesome Developer"
    AUTHOR_EMAIL: str = "awesomedev@dev.com"
    
    API_V1_STR: str = "/api/v1"
    CURRENT_VERSION: str = "0.0.1"
    PROJECT_NAME: str = "Sample API"
    DB_HOST:str = "localhost"
    DB_USERNAME:str = 'username'
    DB_PASSWORD:str = 'password'
    DB_NAME:str = 'database'
    
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 60 * 24 * 8
    SECRET_KEY: str = secrets.token_urlsafe(32)
    
    FIRST_SUPERUSER: str = "admin@admin.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin"
    
settings = Settings()