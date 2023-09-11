from pydantic import  MySQLDsn, validator
from typing import Optional, Dict, Any
from pydantic_settings import BaseSettings

import secrets, os

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    CURRENT_VERSION: str = "0.0.1"
    
    PROJECT_NAME: str
    AUTHOR: str
    AUTHOR_EMAIL: str
    
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str

    MYSQL_HOST:str
    MYSQL_USER:str
    MYSQL_PASSWORD:str
    MYSQL_DATABASE:str
    SQLALCHEMY_DATABASE_URI: Optional[MySQLDsn] = None
    
    @validator("SQLALCHEMY_DATABASE_URI")
    def get_db_url(cls, v:Optional[str], values: Dict[str, Any]):

        if isinstance(v, str):
            return v
        return MySQLDsn.build(
            scheme="mysql",
            username= values.get("MYSQL_USER"),
            password=values.get("MYSQL_PASSWORD"),
            host=values.get("MYSQL_HOST"),
            path=f"{values.get('MYSQL_DATABASE') or ''}",
        )
    
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 60 * 24 * 8
    SECRET_KEY: str = secrets.token_urlsafe(32)
    
settings = Settings()