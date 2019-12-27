from flask import request, Blueprint
from werkzeug.exceptions import (
    BadRequest,
    Conflict,
    NotFound
)
from backend.libs.api_response import (
    STATUS_OK,
    STATUS_CREATED,
    STATUS_NO_CONTENT,
    ApiResponseBody,
    ApiResponse
)


bp = Blueprint('configuration', __name__, url_prefix='/api/configurations')


@bp.route('/', methods=['GET'])
def index():
    pass


@bp.route('/', methods=['PUT'])
def edit():
    pass
