from flask import Flask
from backend.controller import notification
from backend.controller import user


def register_blueprints(app):
    if app is None or not isinstance(app, Flask):
        raise ValueError('Invalid argument: app')
    blueprints = [
        notification.bp,
        user.bp
    ]
    for b in blueprints:
        app.register_blueprint(b)
