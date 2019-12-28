import json
from backend.libs.api_response import (
    STATUS_OK,
    STATUS_CONFLICT,
    STATUS_BAD_REQUEST,
)
from backend.tests.controller.base import BaseApiTestCase


class TestAquariumWaterQuality(BaseApiTestCase):
    END_POINT = '/api/aquarium_water_qualities/'

    def test_index(self):
        res = self.client.get(
            self.END_POINT,
            content_type=self.CONTENT_TYPE
        )
        self.assertEqual(STATUS_OK, res.status_code)
