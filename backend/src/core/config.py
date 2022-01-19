from functools import lru_cache

import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    class ENVIRONMENTS:
        DEVELOPMENT = "development"

    ENVIRONMENT: str
    SITE_DOMAIN: str
    BACKEND_PORT: str
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str

    # Etherscan
    ETHERSCAN_API_KEY: str

    # Postgres
    POSTGRES_DB: str
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    class Config:
        case_sensitive = True

    @property
    def BACKEND_URL(self):
        if self.ENVIRONMENT == self.ENVIRONMENTS.DEVELOPMENT:
            return os.path.join("http://", f"{self.SITE_DOMAIN}:{self.BACKEND_PORT}")

        raise NotImplementedError(f"Incorrect environment or return value not configured for {self.ENVIRONMENT}")


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
