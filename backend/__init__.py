from flask import Flask
from werkzeug.exceptions import (
    BadRequest,
    Conflict,
    Forbidden,
    NotFound,
    InternalServerError,
    Unauthorized
)
from backend.libs.api_error_handler import api_error_handler


app = Flask(__name__)
app.debug = True
app.port = 5000

# Register error handlers
app.register_error_handler(BadRequest, api_error_handler)
app.register_error_handler(Conflict, api_error_handler)
app.register_error_handler(Forbidden, api_error_handler)
app.register_error_handler(NotFound, api_error_handler)
app.register_error_handler(InternalServerError, api_error_handler)
app.register_error_handler(Unauthorized, api_error_handler)
