from datetime import datetime
from datetime import timedelta

from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for

from pocket_auth import authorize_user
from pocket_auth import get_authentication_url
from pocket_retrive import get_read_articles_from_datetime


_APP = Flask(__name__)


_DEFAULT_LATEST_DAYS = 7


@_APP.route("/")
def authentication():
    response = render_template(
        'index.html',
        authentication_url=get_authentication_url(),
    )
    return response


@_APP.route("/proxy")
def authentification_proxy():
    access_token = authorize_user()
    return redirect(
        url_for('view_read_articles', access_token=access_token),
    )


@_APP.route("/<string:access_token>/articles")
@_APP.route("/<string:access_token>/articles/days/<int:days>")
def view_read_articles(access_token, days=None):
    if not days:
        days = _DEFAULT_LATEST_DAYS
    date_time = datetime.today() - timedelta(days=days)
    print date_time
    read_articles = \
        get_read_articles_from_datetime(access_token, date_time)
    return render_template(
        'read_articles.html',
        read_articles=read_articles,
        days_since=days,
    )


if __name__ == "__main__":
    _APP.run(debug=True)
