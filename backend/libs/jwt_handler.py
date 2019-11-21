"""
    jwt_handler.py
    This module implement Flask-JWT-extended callback functions

    Author: Kenta Yamada
    Refferces
      https://flask-jwt-extended.readthedocs.io/en/stable/
      https://flask-jwt-extended.readthedocs.io/en/stable/changing_default_behavior/#changing-callback-functions
"""
from flask import request


def get_auth_token():
    if request is None:
        raise ValueError('request object is null')

    auth = request.headers.get('Authorization', type=str)
    if not auth:
        raise ValueError('Failed get auth token')

    auth_type, auth_token = auth.split(' ')
    return auth_token


def user_loader_handler(identity):
    """
        user_loader_callback_loader callback function
    """
    pass


def user_loader_error_handler(identity):
    """
        user_loader_error_loader callback function
    """
    pass


def token_in_blacklist_loader_handler(decoded_jwt):
    """
        token_blacklist_loader callback function
    """
    pass
