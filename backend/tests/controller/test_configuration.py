import json
from urllib.parse import urljoin
from backend.libs.api_response import (
    STATUS_OK,
    STATUS_CREATED,
    STATUS_CONFLICT,
    STATUS_BAD_REQUEST,
    STATUS_METHOD_NOT_ALLOWED,
    STATUS_NOT_FOUND,
    STATUS_NO_CONTENT
)
from backend.tests.controller.base import BaseApiTestCase


class TestConfigurationApi(BaseApiTestCase):
    pass
