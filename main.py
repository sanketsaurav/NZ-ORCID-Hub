# -*- coding: utf-8 -*-
"""Application module gluing script.

Simple solution to overcome circular import problem:
http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/
"""

import logging
import os

import click
import initializedb
import models  # noqa: F401
from application import app
from authcontroller import *  # noqa: F401, F403
from flask_debugtoolbar import DebugToolbarExtension
from reports import *  # noqa: F401, F403
from views import *  # noqa: F401, F403


@app.before_first_request
def setup_logging():
    app.logger.setLevel(logging.INFO)


@app.cli.command()
def initdb():
    """Initialize the database."""
    initializedb.initdb()


@app.cli.command()
@click.argument('filename')
def load_org_info(filename):
    """Pre-loads organisation data."""
    row_count = models.OrgInfo.load_from_csv(filename)
    print("Loaded %d records" % row_count)


if os.environ.get("ENV") == "dev0":
    # This allows us to use a plain HTTP callback
    os.environ['DEBUG'] = "1"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.debug = True

if app.debug:
    toolbar = DebugToolbarExtension(app)
    # logger = logging.getLogger('peewee')
    # logger.setLevel(logging.DEBUG)
    # logger.addHandler(logging.StreamHandler())

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['DEBUG'] = "1"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ["ENV"] = "dev0"
    app.debug = True
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8000)
