from flask import Flask
from werkzeug.exceptions import (
    BadRequest,
    Conflict,
    Forbidden,
    NotFound,
    InternalServerError,
    Unauthorized
)
from backend.config import get_config_by_env
from backend.libs.api_error_handler import api_error_handler
from backend.controller import register_blueprints


# Create entry point
config = get_config_by_env()

app = Flask(__name__)
app.config.from_object(config)

# Register handlers
app.register_error_handler(BadRequest, api_error_handler)
app.register_error_handler(Conflict, api_error_handler)
app.register_error_handler(Forbidden, api_error_handler)
app.register_error_handler(NotFound, api_error_handler)
app.register_error_handler(InternalServerError, api_error_handler)
app.register_error_handler(Unauthorized, api_error_handler)

# Register blueprints
register_blueprints(app)
