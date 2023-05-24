import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import time
import random
from config import Token

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

args = []


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
        'hello, flip a coin please - /flip\npercent chance of a side of the coin coming up - /static')


async def flip_coin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global args
    args.append(random.randint(1, 2))
    await update.message.reply_text('flip a coin...')
    time.sleep(1)
    await update.message.reply_text(f'came up {"tail" if args[-1] == 1 else "eagle"}')


async def static_coins(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = calculate_coins(args)
    await update.message.reply_text(answer)


def main() -> None:
    application = Application.builder().token(Token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("flip", flip_coin))
    application.add_handler(CommandHandler("static", static_coins))
    application.run_polling()


if __name__ == "__main__":
    main()
