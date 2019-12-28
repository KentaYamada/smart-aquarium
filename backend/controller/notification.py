from flask import Blueprint
from backend.libs.api_response import (
    STATUS_OK,
    ApiResponse,
    ApiResponseBody
)
from backend.mapper.notification import NotificationMapper


bp = Blueprint('notification', __name__, url_prefix='/api/notifications')


@bp.route('/', methods=['GET'])
def index():
    notifications = NotificationMapper.find()
    body = ApiResponseBody()
    body.notifications = notifications
    return ApiResponse(STATUS_OK, body)
