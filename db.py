from telegram import Update
from config import REDIS_DB
import json


def set_info_db(update: Update, args: list) -> None:
    REDIS_DB.mset({update.message.from_user.id: json.dumps(args)})


def get_info_db(update: Update) -> list:
    answer = REDIS_DB.get(update.message.from_user.id)
    return json.loads(answer)
