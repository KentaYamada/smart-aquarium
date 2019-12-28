from flask import Flask
from backend.controller import aquarium_water_quality
from backend.controller import configuration
from backend.controller import notification


def register_blueprints(app):
    if app is None or not isinstance(app, Flask):
        raise ValueError('Invalid argument: app')
    blueprints = [
        aquarium_water_quality.bp,
        configuration.bp,
        notification.bp,
    ]
    for b in blueprints:
        app.register_blueprint(b)
