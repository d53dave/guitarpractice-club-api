from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    OAUTH_SECRET: str
    GOOGLE_CONF_URL: str = 'https://accounts.google.com/.well-known/openid-configuration'
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URL: str

    TOKEN_TIMEOUT_HOURS: int = 336  # 2 Weeks

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"
