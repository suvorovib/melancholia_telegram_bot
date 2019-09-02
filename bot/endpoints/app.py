from ..config import Config as config
from flask import Flask
from ..bot_essential import MelancholyBot

app = Flask(__name__)


def run():
    mbot = MelancholyBot(token=config.TOKEN)
    mbot.set_up_webhook(url=config.WEBHOOK_URL, sert=config.SERT_PATH)
