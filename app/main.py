from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.init_db import init_db

init_db()


description = """
Fast API Template
"""

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.CURRENT_VERSION,
    description= description,
    contact={
        "name"  : settings.AUTHOR,
        "email" : settings.AUTHOR_EMAIL
    }
)

app.include_router(api_router, prefix=settings.API_V1_STR)