from pydantic import BaseSettings

from typing import Optional


class Settings(BaseSettings):
    DATABASE_URL: str
    OAUTH_SECRET: str
    GOOGLE_CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URL: str