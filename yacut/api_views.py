import re

from flask import jsonify, request, url_for

from . import app, db
from .models import URL_map
from .error_handlers import InvalidAPIUsage
from .utils import get_unique_short_id
from .constants import PATTERN


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса', 400)
    original = data.get('url')
    if original is None:
        raise InvalidAPIUsage('"\"url\" является обязательным полем!')
    short = data.get('custom_id')
    if URL_map.query.filter_by(short=short).first() is not None:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if not re.match(PATTERN, short):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if short is None:
        short = get_unique_short_id()
    url_link = URL_map(
        original=original,
        short=short
    )
    db.session.add(url_link)
    db.session.commit()
    response_dict = {
        'url': original,
        'short_link': url_for(
            'redirect_to_url', short_url=short, _external=True
        ),
    }
    return jsonify(response_dict), 201
