# flake8: noqa
from authlib.client.flask import OAuth
from .base import Base, db
from .user import User, Connect, get_current_user, fetch_token

oauth = OAuth(fetch_token=fetch_token)