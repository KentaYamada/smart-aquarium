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
from backend.mapper.black_list import BlackListMapper
from backend.mapper.user import UserMapper


bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data is None:
        raise BadRequest()

    allow_fields = {'email', 'password'}
    if not data.keys() >= allow_fields:
        raise BadRequest()

    user = UserMapper.find_user_by_email('test')
    if user is None:
        raise Unauthorized()

    is_match = user.verify_password(data['password'])
    if not is_match:
        raise Unauthorized(description='Password unmatch')

    logged_in_token = AuthMapper.get_logged_in_user_token(user.id)
    if logged_in_token:
        response = {'logged_in': True, 'token': logged_in_token}
        return ApiResponse(STATUS_OK, 'Already logged in', response)

    token = AuthMapper.generate_auth_token(user)
    if not token:
        raise InternalServerError(description='Failed publish token')

    response = {'logged_in': True, 'token': token}
    return ApiResponse(STATUS_OK, 'Login successfully', response)


@bp.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    if data is None:
        raise BadRequest()

    allow_fields = {'token'}
    if not data.keys() >= allow_fields:
        raise BadRequest('Invalid fields')

    # dispose token & add black list
    is_disposed = AuthMapper.dispose_token(data['token'])
    if not is_disposed:
        raise InternalServerError(description='Failed dispose token')

    response = {'logged_out': True, 'token': ''}
    return ApiResponse(STATUS_OK, 'Logged out', response)


@bp.route('/reflesh', methods=['POST'])
def reflesh():
    data = request.get_json()
    if data is None:
        raise BadRequest(description='Request has empty data')

    allow_fields = {'token'}
    if not data.keys() >= allow_fields:
        raise BadRequest('Request data has invalid fields')

    is_black_list = BlackListMapper.token_in_black_list(data['token'])
    if is_black_list:
        raise BadRequest(description='Token in blacklist')

    auth_data = AuthMapper.find_by_token(data['token'])
    if auth_data is None:
        raise BadRequest(description='Invalid token')

    reflesh_token = AuthMapper.generate_auth_token(auth_data)
    if not reflesh_token:
        raise InternalServerError(description='Failed publish token')

    # dispose token & add black list
    is_disposed = AuthMapper.dispose_token(data['token'])
    if not is_disposed:
        raise InternalServerError(description='Failed dispose token')

    response = {'token': reflesh_token}
    return ApiResponse(STATUS_OK, data=response)
