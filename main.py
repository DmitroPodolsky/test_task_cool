from loguru import logger
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import time
import random
from config import settings
from db import set_info_db, get_info_db
import json
from db import set_info_db,get_info_db


def calculate_coins(args: list) -> str:
    tails = args.count(1)
    eagle = args.count(2)
    try:
        final = round(100 / (tails + eagle))
    except ZeroDivisionError:
        return f"tails = 0%\n eagle = 0%\n maybe you want more flip coin - /flip"
    tails *= final
    eagle *= final
    return f"tails = {tails}%\n eagle = {eagle}%\n maybe you want more flip coin - /flip"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'hello, flip a coin please - /flip\npercent chance of a side of the coin coming up - /static')
    set_info_db(update, [])
    logger.success('start message completed')


async def flip_coin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data_info = get_info_db(update)
    data_info.append(random.randint(1, 2))
    await update.message.reply_text('flip a coin...')
    time.sleep(1)
    await update.message.reply_text(f'came up {"tail" if data_info[-1] == 1 else "eagle"}')
    set_info_db(update, data_info)
    logger.success('flip completed')


async def static_coins(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data_info = get_info_db(update)
    answer = calculate_coins(data_info)
    await update.message.reply_text(answer)
    logger.success('static completed')


def main() -> None:
    application = Application.builder().token(settings.BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("flip", flip_coin))
    application.add_handler(CommandHandler("static", static_coins))
    logger.success('script started')
    application.run_polling()


if __name__ == "__main__":
    main()
