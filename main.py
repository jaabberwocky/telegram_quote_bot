from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import configparser
import logging
from datetime import datetime
import pytz
from telegramScrapper import Scrapper

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO,
    filename='telegram_bot.log'
)

logging.debug('Reading credentials and loading bot...')
cfg = configparser.ConfigParser()
cfg.read('config.cfg')
TOKEN = cfg['DEFAULT']['token'] # insert your bot token here
logging.info('Credentials established.')


logging.info('Log file established.')

logging.info('Starting bot.')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

singapore = pytz.timezone('Asia/Singapore')
scrapper = Scrapper()

# callback functions

## common message
MSG = "Say '/time' for time or '/quote' to get a quote!"

## callbacks
def start(update, context):
    welcome_text = "Hello {}, I am a bot and do start talking to me!\n\nSay what you want and I'll try to respond! \nSay '/time' to get the current time\nSay '/quote' for me to say something random.".format(str(update.message.from_user.username))
    context.bot.send_message(
        chat_id = update.effective_chat.id, 
        text=welcome_text
    )
    logging.info('{}: {}'.format(update.effective_chat.id, welcome_text))

def echo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text="I didn't understand that but my creator loves you!")
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text=MSG
    )

def whatTime(update, context):
    now = datetime.now(singapore).time().strftime("%H:%M:%S")
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text="The time now is: {}".format(now)
    )
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text=MSG
    )

def sayQuote(update, context):
    msg = scrapper.getQuote()
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text=msg
    )
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text=MSG
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