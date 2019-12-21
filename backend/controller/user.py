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
    ApiResponse,
    ApiResponseBody
)
from backend.mapper.user import UserMapper
from backend.model.user import User


bp = Blueprint('user', __name__, url_prefix='/api/users')


@bp.route('/', methods=['GET'])
def index():
    users = UserMapper.find_users()
    body = ApiResponseBody()
    body.users = users
    return ApiResponse(STATUS_OK, data=body)


@bp.route('/', methods=['POST'])
def add():
    data = request.get_json()
    if data is None:
        raise BadRequest()

    allow_fields = {'id', 'name', 'email', 'password'}
    if not data.keys() >= allow_fields:
        raise BadRequest()

    user = User(**data)
    saved = UserMapper.save(user)
    if not saved:
        raise Conflict(description='Failed add data')

    body = ApiResponseBody()
    body.message = 'created'
    body.result = True
    return ApiResponse(STATUS_CREATED, body)


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    data = request.get_json()
    if data is None:
        raise BadRequest()

    allow_fields = {'id', 'name', 'email', 'password'}
    if not data.keys() >= allow_fields:
        raise BadRequest()

    is_exist = UserMapper.exist_user(id)
    if not is_exist:
        raise NotFound(description='Not exist user')

    user = User(**data)
    saved = UserMapper.save(user)
    if not saved:
        raise Conflict(description='Failed edit data')

    body = ApiResponseBody()
    body.message = 'edited'
    body.result = True
    return ApiResponse(STATUS_OK, body)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    deleted = UserMapper.delete(id)
    if not deleted:
        raise NotFound(description='Not exist user')
    return ApiResponse(STATUS_NO_CONTENT)
