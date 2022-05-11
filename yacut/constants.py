from string import ascii_letters, digits


'''Константы'''
SYMBOLS = f'{ascii_letters}{digits}'
MAX_LEN_SHORT_URL = 16
MIN_LEN_SHORT_URL = 1
LEN_SHORT_URL = 6
PATTERN = rf'^[{SYMBOLS}]+$'

'''Сообщения'''
NAME_BUSY = 'Имя {} уже занято!'
URL_READY = 'Ваша новая ссылка готова:'

EMPTY_REQUEST = 'Отсутствует тело запроса'
REQ_FIELD = '\"url\" является обязательным полем!'
BAD_NAMING = 'Указано недопустимое имя для короткой ссылки'
NO_ID = 'Указанный id не найден'
API_NAME_BUSY = 'Имя "{}" уже занято.'
