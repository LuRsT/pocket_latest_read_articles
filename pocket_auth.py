from requests import post as make_post_request
from urllib import urlencode

from constants import JSON_HEADERS
from constants import POCKET_CONSUMER_KEY
from constants import REDIRECT_URL
from requests_utils import get_endpoint_url


def authorize_user():
    data = {
        'consumer_key': POCKET_CONSUMER_KEY,
        'code': _CODE,
    }
    request = make_post_request(
        get_endpoint_url('oauth/authorize'),
        headers=JSON_HEADERS,
        json=data,
    )
    if request.status_code == 200:
        access_token = request.json()['access_token']
    else:
        access_token = None
    return access_token


def _get_user_code():
    data = {
        'consumer_key': POCKET_CONSUMER_KEY,
        'redirect_uri': REDIRECT_URL,
    }
    request = make_post_request(
        get_endpoint_url('oauth/request'),
        json=data,
        headers=JSON_HEADERS,
    )

    if request.status_code == 200:
        user_code = request.json()['code']
    else:
        user_code = None
    return user_code


def get_authentication_url():
    url_params = {
        'redirect_uri': REDIRECT_URL,
        'request_token': _CODE,
    }
    url_params_encoded = urlencode(url_params)
    authentication_url = '?'.join((
        'https://getpocket.com/auth/authorize',
        url_params_encoded,
    ))
    return authentication_url


_CODE = _get_user_code()
