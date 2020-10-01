from pydantic import BaseSettings

from typing import Optional


class Settings(BaseSettings):
    DATABASE_URL: str