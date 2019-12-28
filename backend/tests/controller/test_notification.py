import json
from backend.libs.api_response import STATUS_OK
from backend.tests.controller.base import BaseApiTestCase


class TestNotificationApi(BaseApiTestCase):
    END_POINT = '/api/notifications/'

    def test_index(self):
        res = self.client.get(
            self.END_POINT,
            content_type=self.CONTENT_TYPE
        )
        self.assertEqual(STATUS_OK, res.status_code)
