from urlparse import urljoin as url_join

from constants import POCKET_BASE_URL


def get_endpoint_url(url_part):
    return url_join(POCKET_BASE_URL, url_part)
