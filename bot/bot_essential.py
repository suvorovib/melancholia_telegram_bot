from .config import Config as config
from typing import List
import logging
from telegram import Bot, error
import requests

logger = logging.getLogger('bot_essential')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class UpdateTypes:

    message = 'message'
    edited_message = 'edited_message'
    channel_post = 'channel_post'
    edited_channel_post = 'edited_channel_post'
    inline_query = 'inline_query'
    chosen_inline_result = 'chosen_inline_result'
    callback_query = 'callback_query'
    shipping_query = 'shipping_query'
    pre_checkout_query = 'pre_checkout_query'
    poll = 'poll'


def make_request(method: str, url: str) -> dict:
    response = requests.request(method, url)
    if response.status_code == 200:
        data_json = response.json()
    else:
        # TODO add exceptions
        data_json = {}

    return data_json


class MelancholyBot(Bot):
    def __init__(self, *args, **kwargs):
        super(MelancholyBot, self).__init__(args, kwargs)
        self.check_bot()

    def check_bot(self) -> bool:
        try:
            response = self.get_me()
        except error.Unauthorized:
            return False

        level = logging.INFO

        if response is None:
            logger.log(level, 'Token invalid')
            return False
        else:
            logger.log(level, f'Token valid bot. Bot name: {response.name}, id {response.id}, link: {response.link}')
            return True

    def set_up_webhook(self, url: str, sert: object = None, timeout: int = 60,  max_connections: int = 40,
                         allowed_updates: List[str] = None):
        response = self.set_webhook(url, sert, timeout, max_connections, allowed_updates)
        if not response:
            logger.error('Failed to connect webhook for bot')
        else:
            logger.info('Webhook successfully set up')

    def close_webhook(self):
        self.set_webhook(url='')
        logger.info('Webhook successfully closed')

    def get_btc_price(self, pair: str = 'USD'):
        response = make_request('GET', config.BTC_PRICE_URL)
        pair_prices = response.get(pair, {})
        buy_price = pair_prices.get('buy', None)
        sell_price = pair_prices.get('sell', None)

        if buy_price is not None and sell_price is not None:
            pair_symbol = pair_prices.get('symbol', None)

            return f'1 BTC buy price: {buy_price}{pair_symbol}, sell price: {sell_price}{pair_symbol} '
        else:
            return 'Bad response reached, call 911'
