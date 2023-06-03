from typing import Optional
from redis import StrictRedis
from pydantic import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str = 'redis'
    REDIS_PORT: int = 6379
    BOT_TOKEN: Optional[str]

    class Config:
        env_file = '.env'
        case_sensitive = True


settings = Settings()
REDIS_DB = StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True)
