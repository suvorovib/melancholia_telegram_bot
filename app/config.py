import os
class Config:

    HOST = '0.0.0.0'
    PORT = 80

    TOKEN = os.environ.get('TOKEN')

    BTC_PRICE_URL = 'https://blockchain.info/ticker'

    WEBHOOK_URL = f'https://melanholia.host/{TOKEN}'
    SERT_PATH = None
