import json
from unittest.mock import patch
from backend.libs.api_response import (
    STATUS_OK,
    STATUS_BAD_REQUEST,
    STATUS_INTERNAL_SERVER_ERROR
)
from backend.tests.controller.base import BaseApiTestCase


class TestAuthApi(BaseApiTestCase):
    @patch('backend.mapper.auth.AuthMapper.dispose_token')
    def test_logout_success(self, mock_dispose_token):
        mock_dispose_token.return_value = True
        res = self.client.post(
            '/api/auth/logout',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'token': 'test'})
        )
        self.assertEqual(STATUS_OK, res.status_code)

    @patch('backend.mapper.auth.AuthMapper.dispose_token')
    def test_logout_when_dispose_token_failure(self, mock_dispose_token):
        mock_dispose_token.return_value = False
        res = self.client.post(
            '/api/auth/logout',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'token': 'test'})
        )
        self.assertEqual(STATUS_INTERNAL_SERVER_ERROR, res.status_code)

    def test_logout_when_request_is_null(self):
        res = self.client.post(
            '/api/auth/logout',
            content_type=self.CONTENT_TYPE,
            data=None
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_logout_when_request_is_empty_data(self):
        res = self.client.post(
            '/api/auth/logout',
            content_type=self.CONTENT_TYPE,
            data={}
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_logout_when_post_invalid_field(self):
        res = self.client.post(
            '/api/auth/logout',
            content_type=self.CONTENT_TYPE,
            data={'hoge': 'fuga'}
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_logout_when_token_is_empty(self):
        with self.assertRaises(ValueError):
            for v in ('', None):
                self.client.post(
                    '/api/auth/logout',
                    content_type=self.CONTENT_TYPE,
                    data=json.dumps({'token': v})
                )
