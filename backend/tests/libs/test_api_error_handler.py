import unittest
from werkzeug.exceptions import (
    NotFound
)
from backend.libs.api_error_handler import api_error_handler
from backend.libs.api_response import (
    STATUS_NOT_FOUND,
    STATUS_INTERNAL_SERVER_ERROR
)


class TestApiErrorHandler(unittest.TestCase):
    def test_api_error_handler(self):
        res = api_error_handler(NotFound())
        self.assertEqual(STATUS_NOT_FOUND, res.status_code)

    def test_api_error_handler_when_arg_is_null(self):
        res = api_error_handler(None)
        self.assertEqual(STATUS_INTERNAL_SERVER_ERROR, res.status_code)
