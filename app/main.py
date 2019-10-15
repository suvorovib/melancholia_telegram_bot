from .config import Config as config
from flask import Flask, request
import logging
from .bot_essential import MelancholyBot
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASS}' \
                                        f'@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}'
db = SQLAlchemy(app)
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
    user_first_name = chat.get('first_name')
    if text == '/btc':
        btc_price = mbot.get_btc_price()
        text = btc_price
    if text == '/start':
        text = mbot.get_start_message(user_first_name)
    mbot.send_message(chat_id, text)
    return 'OK', 200


def run():
    try:
        mbot.set_up_webhook(url=config.WEBHOOK_URL, sert=config.SERT_PATH)
        app.run(host=config.HOST, port=config.PORT, debug=True)
    finally:
        mbot.delete_webhook()
        pass
