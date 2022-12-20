import config
import numpy as np
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler


CMD_RANDINT_AB = "np.randint"
CMD_RANDOM_01 = "np.random"

def get_value(cmd):
    if cmd == "1":
        return np.random.randint(0, int(1e9))
    elif cmd == "2":
        return np.random.random()
    return "Error"


async def start(update, context):
    await update.message.reply_text(f"Hello, {update.message.chat.username}!\nUse command /help to check bot commands!")


async def get_random(update, context):
    keyboard = [[
            InlineKeyboardButton(CMD_RANDINT_AB, callback_data="1"),
            InlineKeyboardButton(CMD_RANDOM_01, callback_data="2"),
    ]]
    await update.message.reply_text("Please choose random type:", reply_markup=InlineKeyboardMarkup(keyboard))


async def button(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Random result: {get_value(query.data)}")


async def helpcmd(update, context):
    await update.message.reply_text("/start - начало работы бота\n/get_random - получить следующее рандомное число\n/askbot - бот ответит на свой же вопрос\n/help - расскажет о себе")

async def askbot(update, context):
    await update.message.reply_text("Is this the coolest bot ever?\n")
    time.sleep(1)
    await update.message.reply_text("Yes!\n")


if __name__ == "__main__":
    application = Application.builder().token(config.TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get_random", get_random))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", helpcmd))
    application.add_handler(CommandHandler("askbot", askbot))
    application.run_polling()