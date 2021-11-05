from fastapi import FastAPI

from src.apps.users import models
from src.core.api_routing import api_router
from src.core.config import settings
from src.core.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)
