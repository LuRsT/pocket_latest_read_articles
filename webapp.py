from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for

from pocket_auth import authorize_user
from pocket_auth import get_authentication_url
from pocket_retrive import get_latest_read_articles


_APP = Flask(__name__)


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
        url_for('view_latest_read_articles', access_token=access_token),
    )


@_APP.route("/<string:access_token>/articles")
def view_latest_read_articles(access_token):
    latest_read_articles = get_latest_read_articles(access_token)
    return render_template(
        'latest_posts.html',
        latest_read_articles=latest_read_articles,
    )


if __name__ == "__main__":
    _APP.run(debug=True)
