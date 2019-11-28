from backend.libs.api_response import (
    STATUS_INTERNAL_SERVER_ERROR,
    ApiResponse
)


def api_error_handler(error):
    """
        Flask register_error_handler callback function
    """
    if error is None:
        return ApiResponse(
            STATUS_INTERNAL_SERVER_ERROR,
            'Internal Server Error'
        )

    message = ''
    if hasattr(error, 'description') and error.description:
        message = error.description

    errors = None
    if hasattr(error, 'response') and error.response is not None:
        errors = error.response

    return ApiResponse(error.code, message, errors=errors)
