from requests import get as make_get_request
from time import mktime

from constants import POCKET_CONSUMER_KEY
from requests_utils import get_endpoint_url


def get_read_articles_from_datetime(access_token, date_time):
    params = {
        'access_token': access_token,
        'consumer_key': POCKET_CONSUMER_KEY,

        'since': mktime(date_time.timetuple()),
        'detailType': 'simple',
        'state': 'archive',
    }
    request = make_get_request(
        get_endpoint_url('get'),
        params=params,
    )
    formatted_articles = _format_articles(request.json())
    return formatted_articles


def _format_articles(data):
    articles_list = data['list']
    articles = [v for i, v in articles_list.items()]
    return articles
