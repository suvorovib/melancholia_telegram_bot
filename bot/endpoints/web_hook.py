from ..endpoints import app
from flask import request
from ..config import Config as config
import logging


logger = logging.getLogger('webhook_route')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@app.route(f'/{config.TOKEN}', methods=['POST'])
def webhook_route(*args):
    logger.info(request.json)
    return 'OK', 200
