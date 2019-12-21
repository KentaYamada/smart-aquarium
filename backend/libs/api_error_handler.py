from backend.libs.api_response import (
    STATUS_INTERNAL_SERVER_ERROR,
    ApiResponse,
    ApiResponseBody
)


def api_error_handler(error):
    """
        Flask register_error_handler callback function
    """
    body = ApiResponseBody()
    if error is None:
        body.message = 'Internal Server Error'
        return ApiResponse(STATUS_INTERNAL_SERVER_ERROR, body)
    if hasattr(error, 'description') and error.description:
        body.message = error.description
    if hasattr(error, 'response') and error.response is not None:
        body.errors = error.response
    return ApiResponse(error.code, body)
