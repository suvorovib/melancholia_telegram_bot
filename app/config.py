import os


class Config:

    HOST = '0.0.0.0'
    PORT = 80

    TOKEN = os.environ.get('TOKEN')

    BTC_PRICE_URL = 'https://blockchain.info/ticker'

    WEBHOOK_URL = f'https://melanholia.host/{TOKEN}'
    SERT_PATH = None

    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', '0.0.0.0')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5432')
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_PASS = os.environ.get('POSTGRES_PASS', 'SomeDBPass')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'melancholia')
