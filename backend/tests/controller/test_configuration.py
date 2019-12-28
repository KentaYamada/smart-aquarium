import json
from unittest.mock import patch
from backend.libs.api_response import (
    STATUS_OK,
    STATUS_CONFLICT,
    STATUS_BAD_REQUEST,
)
from backend.tests.controller.base import BaseApiTestCase


class TestConfigurationApi(BaseApiTestCase):
    END_POINT = '/api/configurations/'

    def test_index(self):
        res = self.client.get(
            self.END_POINT,
            content_type=self.CONTENT_TYPE
        )
        self.assertEqual(STATUS_OK, res.status_code)

    def test_apply(self):
        data = json.dumps({
            'ph_lower_limit': 6.7,
            'ph_upper_limit': 6.9,
            'temperature_lower_limit': 23.0,
            'temperature_upper_limit': 23.5,
            'measurement_trials': 3
        })
        res = self.client.post(
            self.END_POINT,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_OK, res.status_code)
        self.assertTrue(body['result'])
        self.assertEqual(body['message'], '設定反映しました')

    def test_apply_failure_when_request_no_data(self):
        res = self.client.post(
            self.END_POINT,
            content_type=self.CONTENT_TYPE,
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_apply_failure_when_invalid_request_data(self):
        data = json.dumps({
            'ph_lower_limit': 6.7,
            'temperature_lower_limit': 23.0,
            'measurement_trials': 3
        })
        res = self.client.post(
            self.END_POINT,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)
        self.assertEqual(body['message'], '不正なリクエストです')

    @patch('backend.mapper.configuration.ConfigurationMapper.save')
    def test_apply_failure_when_save_failed(self, mock_save):
        mock_save.return_value = False
        data = json.dumps({
            'ph_lower_limit': 6.7,
            'ph_upper_limit': 6.9,
            'temperature_lower_limit': 23.0,
            'temperature_upper_limit': 23.5,
            'measurement_trials': 3
        })
        res = self.client.post(
            self.END_POINT,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_CONFLICT, res.status_code)
        self.assertEqual(body['message'], '設定の反映に失敗しました')
