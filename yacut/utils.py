import random

from . import constants as cst
from .models import URL_map


def get_unique_short_id(symbols=cst.SYMBOLS,
                        length=cst.LEN_SHORT_URL):
    url_link = ''
    for char in range(length):
        url_link += random.choice(symbols)
    return url_link


def check_short_url(short_url):
    return bool(URL_map.query.filter_by(short=short_url).first())
