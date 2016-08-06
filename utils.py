import telegram

DOMAIN = 'http://www.busevi.com'
BUS_URL = "{}/images/stories/Red-Voznje/Gradski-Prevoz-BG/linija.{}-{}.png"
BG_TRAIN_URL = '{}/images/stories/Red-Voznje/bgvoz-beovoz/bgvoz-{}.png'
MINIBUS_URL = '{}/images/stories/Red-Voznje/Citybus/linija-{}-{}.png'
NIGHT_BUS_URL = '{}/images/stories/Red-Voznje/Nocne%20linije%20(Beograd)/linija.{}.png'

BG_TRAIN_MAPPING = {
    "batajnica": 1,
    "pancevacki": 2
}

with open("help-start-text.txt", 'r') as f:
    START_HELP_TXT = f.read()


def start(bot, update):
    url = START_HELP_TXT
    bot.sendMessage(update.message.chat_id, text=url.encode('UTF-8'), parse_mode=telegram.ParseMode.MARKDOWN)


def help(bot, update):
    url = START_HELP_TXT
    bot.sendMessage(update.message.chat_id, text=url.encode('UTF-8'), parse_mode=telegram.ParseMode.MARKDOWN)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=START_HELP_TXT, parse_mode=telegram.ParseMode.MARKDOWN)