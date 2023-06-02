import dotenv
from redis import StrictRedis
from pydantic import BaseSettings

TOKEN = dotenv.dotenv_values(".env")['Token']  # Your_token
REDIS_DB = StrictRedis(host='redis', port=6379, db=0, decode_responses=True)


class Settings(BaseSettings):
    TOKEN: str = TOKEN
    REDIS_DB: str = REDIS_DB

