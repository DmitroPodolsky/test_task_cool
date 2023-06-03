import dotenv
from redis import StrictRedis
from pydantic import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str = 'redis'
    REDIS_PORT: int = 6379

    class Config:
        env_file = '.env'
        case_sensitive = True


settings = Settings()
TOKEN = dotenv.dotenv_values(settings.Config.env_file)['Token']  # Your_token
REDIS_DB = StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True)
