# default values

ENGINE = 'futures'
MARKET = 'forts'
BOARD = 'RFUD'
SECURITY = 'SiM3'

# json respone keys
JSON_CANDLES_KEY = 'candles'

# path
DEFAULT_REQUEST_TEMPLATE = 'http://iss.moex.com/iss/{path}?{params}'
CANDLES_PATH = 'engines/{engine}/markets/{market}/boards/{board}/securities/{security}/candles.json'
