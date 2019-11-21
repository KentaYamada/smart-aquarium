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
STATUS_CONFLICT = 409
STATUS_INTERNAL_SERVER_ERROR = 500


class ApiResponse(Response):
    """
        REST API response class
    """
    def __init__(self, status_code, message='', data=None, errors=None):
        super().__init__()
        self.mimetype = 'application/json'
        self.status_code = status_code
        body = self.__get_response_body(message, data, errors)
        self.set_data(body)

    def __get_response_body(self, message, data, errors):
        body = {
            'data': data,
            'errors': errors,
            'message': message
        }
        return json.dumps(body, ensure_ascii=False, indent=2)
