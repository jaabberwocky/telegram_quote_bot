from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import configparser
import logging
from datetime import datetime
from getQuotes import GetQuote

cfg = configparser.ConfigParser()
cfg.read('config.cfg')
TOKEN = cfg['DEFAULT']['token']

print("logging...")
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

print("starting bot...")
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# functionality
def start(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id, 
        text="Hello {}, I am a bot and do start talking to me!\n\nSay what you want and I'll try to respond! \nSay '/time' to get the current time\nSay '/quote' for me to say something random.".format(str(update.message.from_user.username))
    )

def echo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text="I didn't understand that but my creator loves you! <3")

def whatTime(update, context):
    now = datetime.now().time().strftime("%H:%M:%S")
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text="The time now is: {}".format(now)
    )

def sayQuote(update, context):
    msg = GetQuote()
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text=msg
    )

# handlers
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
time_handler = CommandHandler('time', whatTime)
quote_handler = CommandHandler('quote', sayQuote)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(time_handler)
dispatcher.add_handler(quote_handler)

updater.start_polling()