from os import environ


POCKET_CONSUMER_KEY = environ['POCKET_CONSUMER_KEY']
REDIRECT_URL = 'http://localhost:5000/proxy'
POCKET_BASE_URL = 'https://getpocket.com/v3/'

JSON_HEADERS = {
    'content-type': 'application/json; charset=UTF-8',
    'x-accept': 'application/json'
}