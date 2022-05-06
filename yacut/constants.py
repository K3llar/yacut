from string import ascii_letters, digits

SYMBOLS = f'{ascii_letters}{digits}'

MAX_LEN_SHORT_URL = 16
LEN_SHORT_URL = 6

PATTERN = r'^[a-zA-Z0-9]{1,16}$'
