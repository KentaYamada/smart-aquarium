from flask import request, Blueprint
from werkzeug.exceptions import (
    BadRequest,
    InternalServerError,
    Unauthorized
)
from backend.libs.api_response import (
    STATUS_OK,
    ApiResponse
)
from backend.mapper.auth import AuthMapper


bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    if data is None:
        raise BadRequest()

    allow_fields = {'token'}
    if not data.keys() >= allow_fields:
        raise BadRequest('Invalid fields')

    is_disposed = AuthMapper.dispose_token(data['token'])
    if not is_disposed:
        raise InternalServerError(description='Failed dispose token')

    response = {'logged_out': True, 'token': ''}
    return ApiResponse(STATUS_OK, 'Logged out', response)
