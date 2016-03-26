# pocket_latest_read_articles

Does what it says on the tin, shows you a list of the articles you read on the
last X days (7 is the default).

![screenshot](http://imgur.com/JzDd7epl.png)

## How to use

Conveniently, this project comes with a Docker file so you can use Docker to
use/deploy this.

*Note:* You'll need a Pocket Consumer Key in order to use this, be sure to
change it in the instruction examples.
[How to get it](https://getpocket.com/developer/apps/new)


#### Easy (pulling from dockerhub)

    docker pull lurst/pocket_latest_read_articles
    docker run -d -t -p 5000:5000 -e POCKET_CONSUMER_KEY='YOUR-KEY' lurst/pocket_latest_read_articles
    # Go to your browser at: localhost:5000


#### Bit Harder (if you want to play with the Dockerfile)

    git clone https://github.com/LuRsT/pocket_latest_read_articles.git
    docker build -t pocket_latest_read_articles .
    docker run -d -t -p 5000:5000 -e POCKET_CONSUMER_KEY='YOUR-KEY' pocket_latest_read_articles
    # Go to your browser at: localhost:5000

### Non-Docker way (AKA the old way)

    git clone https://github.com/LuRsT/pocket_latest_read_articles.git
    cd pocket_latest_read_articles
    mkvirtualenv pocket_latest_read_articles
    pip install -r requirements.txt
    POCKET_CONSUMER_KEY='YOUR-KEY' python webapp.py
    # Go to your browser at: localhost:5000

