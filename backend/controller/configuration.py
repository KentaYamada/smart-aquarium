from flask import request, Blueprint
from werkzeug.exceptions import (
    BadRequest,
    Conflict,
    NotFound,
)
from backend.libs.api_response import (
    STATUS_OK,
    ApiResponseBody,
    ApiResponse
)
from backend.mapper.configuration import ConfigurationMapper
from backend.model.configuration import Configuration


bp = Blueprint('configuration', __name__, url_prefix='/api/configurations')


@bp.route('/', methods=['GET'])
def index():
    data = ConfigurationMapper.find()
    if data is None:
        raise NotFound(description='設定情報が見つかりません。')
    body = ApiResponseBody()
    body.configuration = data
    return ApiResponse(STATUS_OK, body)


@bp.route('/', methods=['POST'])
def apply():
    data = request.get_json()
    if data is None:
        raise BadRequest()

    white_list = {
        'ph_lower_limit',
        'ph_upper_limit',
        'temperature_lower_limit',
        'temperature_upper_limit',
        'measurement_trials'
    }
    if not data.keys() >= white_list:
        raise BadRequest(description='不正なリクエストです')

    model = Configuration(**data)
    saved = ConfigurationMapper.save(model)

    if not saved:
        raise Conflict(description='設定の反映に失敗しました')

    body = ApiResponseBody()
    body.message = '設定反映しました'
    body.result = True
    return ApiResponse(STATUS_OK, body)
