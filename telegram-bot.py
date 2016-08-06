import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import TOKEN
from public_transportation import get_bus_schedule, get_train_schedule
from utils import unknown

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# Command config
bus = CommandHandler('bus', get_bus_schedule, pass_args=True)
train = CommandHandler('train', get_train_schedule, pass_args=True)
unknown_handler = MessageHandler([Filters.command], unknown)

# Attaching dispatchers
dispatcher.add_handler(bus)
dispatcher.add_handler(train)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
