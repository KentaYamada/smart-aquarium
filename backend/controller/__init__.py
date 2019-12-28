from flask import Flask
from backend.controller import configuration
from backend.controller import notification


def register_blueprints(app):
    if app is None or not isinstance(app, Flask):
        raise ValueError('Invalid argument: app')
    blueprints = [
        notification.bp,
        configuration.bp,
    ]
    for b in blueprints:
        app.register_blueprint(b)
