from telegram.ext import Updater, CommandHandler
import configparser
import logging

cfg = configparser.ConfigParser()
cfg.read('config.cfg')
TOKEN = cfg['DEFAULT']['token']

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text="I'm a bot, start talking to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()