import logging
from utils import BG_TRAIN_MAPPING, BG_TRAIN_URL, DOMAIN, MINIBUS_URL, BUS_URL, NIGHT_BUS_URL

LOG = logging.getLogger(__name__)


def get_bus_schedule(bot, update, args):
    LOG.debug('Passed arguments: {}'.format(args))
    if len(args) == 1:
        req = args[0]
        for direction in [1, 2]:
            if req.upper().startswith('E'):  # This is a minibus line
                url = MINIBUS_URL.format(DOMAIN, req.lower(), direction)

            elif req.upper().endswith('N'):
                req = req[:-1]  # Strip out N
                url = NIGHT_BUS_URL.format(DOMAIN, req)

                LOG.debug("Request URL is: {}".format(url))
                bot.sendMessage(chat_id=update.message.chat_id, text=url)

                break  # Night buses have only one image for both directions

            else:  # This is a normal bus line
                url = BUS_URL.format(DOMAIN, req.lower(), direction)

            LOG.debug("Request URL is: {}".format(url))
            bot.sendMessage(chat_id=update.message.chat_id, text=url)
    else:
        LOG.warning('Bus number is required! Arguments passed: {}'.format(args))
        bot.sendMessage(chat_id=update.message.chat_id, text='Bus number is required, i.e. /bus 53')


def get_train_schedule(bot, update, args):
    LOG.debug('Passed arguments: {}'.format(args))
    text = 'Allowed values are:\n{}'.format("\n".join(BG_TRAIN_MAPPING.iterkeys()))
    if len(args) == 1:
        try:
            direction = BG_TRAIN_MAPPING[args[0]]
            url = BG_TRAIN_URL.format(DOMAIN, direction)
            LOG.debug("Generated BG_TRAIN url: {}".format(url))
            bot.sendMessage(chat_id=update.message.chat_id, text=url)
        except KeyError:
            LOG.debug("Requested arguments: {}".format(args[0]))
            bot.sendMessage(chat_id=update.message.chat_id, text=text)
    else:
        LOG.warning('Specify starting station. Arguments passed: {}'.format(args))
        bot.sendMessage(chat_id=update.message.chat_id,
                        text='Specify starting station, i.e. /train pancevacki.\n{}'.format(text))

