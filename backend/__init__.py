from flask import Flask
# from flask_jwt_extended import JWTManager
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
# from backend.libs.jwt_handler import (
#     user_loader_handler,
#     user_loader_error_handler,
#     token_in_blacklist_loader_handler
# )
from backend.controller import get_blueprints


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
blueprints = get_blueprints()
for b in blueprints:
    app.register_blueprint(b)

# JWT authorization (if needed)
# jwt = JWTManager(app)

# Register handlers
# jwt.user_loader_callback_loader(user_loader_handler)
# jwt.user_loader_error_loader(user_loader_error_handler)
# jwt.token_in_blacklist_loader(token_in_blacklist_loader_handler)
