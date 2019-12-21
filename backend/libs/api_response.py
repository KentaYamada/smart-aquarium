import json
from flask import Response


# HTTP staus codes
STATUS_OK = 200
STATUS_CREATED = 201
STATUS_NO_CONTENT = 204
STATUS_BAD_REQUEST = 400
STATUS_UNAUTHORIZED = 401
STATUS_FORBIDDEN = 403
STATUS_NOT_FOUND = 404
STATUS_METHOD_NOT_ALLOWED = 405
STATUS_CONFLICT = 409
STATUS_INTERNAL_SERVER_ERROR = 500


def json_dumps_handler(data):
    has_dict = isinstance(data, object) and hasattr(data, '__dict__')
    if not has_dict:
        raise TypeError()
    return data.__dict__


class ApiResponseBody:
    def __init__(self,  message='', errors=None):
        self.message = message
        self.errors = errors


class ApiResponse(Response):
    """
        REST API response class
    """
    def __init__(self, status_code, data=None):
        super().__init__()
        self.mimetype = 'application/json'
        self.status_code = status_code

        if data is not None and not isinstance(data, ApiResponseBody):
            raise TypeError()
        body = json.dumps(
            data,
            default=json_dumps_handler,
            ensure_ascii=False,
            indent=2
        )
        self.set_data(body)
