DOMAIN = 'http://www.busevi.com'

BUS_URL = "{}/images/stories/Red-Voznje/Gradski-Prevoz-BG/linija.{}-{}.png"
BG_TRAIN_URL = '{}/images/stories/Red-Voznje/bgvoz-beovoz/bgvoz-{}.png'
MINIBUS_URL = '{}/images/stories/Red-Voznje/Citybus/linija-{}-{}.png'
NIGHT_BUS_URL = '{}/images/stories/Red-Voznje/Nocne%20linije%20(Beograd)/linija.{}.png'

BG_TRAIN_MAPPING = {
    "batajnica": 1,
    "pancevacki": 2
}


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
