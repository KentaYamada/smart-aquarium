from flask import request, Blueprint
from werkzeug.exceptions import BadRequest
from backend.libs.api_response import (
    STATUS_OK,
    ApiResponse,
    ApiResponseBody
)
from backend.mapper.aquarium_water_quality import (
    AquariumWaterQualityMapper
)
from backend.model.aquarium_water_quality import (
    AquariumWaterQualitySearchOption
)


bp = Blueprint(
    'aquarium_water_quality',
    __name__,
    url_prefix='/api/aquarium_water_qualities'
)


@bp.route('/', methods=['GET'])
def index():
    # if request.args is None:
    #     raise BadRequest()
    # option = AquariumWaterQuqlitySearchOption()
    # data = AquariumWaterQualityMapper.find(option)
    data = AquariumWaterQualityMapper.find()
    body = ApiResponseBody()
    body.water_quarities = data
    return ApiResponse(STATUS_OK, body)
