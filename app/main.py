from .config import Config as config
from flask import Flask, request
import logging
from .bot_essential import MelancholyBot

app = Flask(__name__)
mbot = MelancholyBot(token=config.TOKEN)


logger = logging.getLogger('app')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@app.route('/')
def home():
    return 'Welcome to melancholia', 200


@app.route(f'/{config.TOKEN}', methods=['POST'])
def webhook_route():
    update = request.json
    logger.info(update)
    message = update.get('message')
    text = message.get('text')
    chat = message.get('chat')
    chat_id = chat.get('id')
    if text == '/btc':
        btc_price = mbot.get_btc_price()
        text = btc_price
    mbot.send_message(chat_id, text)
    return 'OK', 200


def run():
    try:
        mbot.get_updates_loop(interim=2)
        mbot.set_up_webhook(url=config.WEBHOOK_URL, sert=config.SERT_PATH)
        app.run(host=config.HOST, port=config.PORT, debug=True)
    finally:
        mbot.delete_webhook()
        pass
