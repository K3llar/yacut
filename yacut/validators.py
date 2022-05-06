import re

from . import constants as cnt


def len_validation(string, exception):
    try:
        getattr(string, '__len__')
    except AttributeError:
        raise AttributeError
    if cnt.MIN_LEN_SHORT_URL <= len(string) <= cnt.MAX_LEN_SHORT_URL:
        return
    raise exception


def regex_validation(string, exception):
    if re.match(cnt.PATTERN, string):
        return
    raise exception
