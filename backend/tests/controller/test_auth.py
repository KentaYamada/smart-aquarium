import json
from unittest.mock import patch, Mock
from backend.libs.api_response import (
    STATUS_OK,
    STATUS_BAD_REQUEST,
    STATUS_INTERNAL_SERVER_ERROR,
    STATUS_UNAUTHORIZED
)
from backend.model.user import User
from backend.tests.controller.base import BaseApiTestCase


class TestAuthApi(BaseApiTestCase):
    @patch('backend.model.user.User')
    @patch('backend.mapper.auth.AuthMapper')
    def test_login_success(self, mock_user, mock_auth_mapper):
        mock_user.find_user_by_email = Mock()
        mock_user.find_user_by_email.return_value = User(
            1, 'Taro', 'taro@email.com', 'taro'
        )
        mock_user.verify_password = Mock()
        mock_user.verify_password.return_value = True
        mock_auth_mapper.get_logged_in_user_token = Mock()
        mock_auth_mapper.return_value = ''
        mock_auth_mapper.generate_auth_token = Mock()
        mock_auth_mapper.generate_auth_token.return_value = 'test_token'
        data = json.dumps({
            'email': 'test@email.com',
            'password': 'test'
        })
        res = self.client.post(
            '/api/auth/login',
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(STATUS_OK, res.status_code)

    @patch('backend.mapper.user.UserMapper.find_user_by_email')
    def test_login_when_not_exist_user(self, mock_find_user_by_email):
        mock_find_user_by_email.return_value = None
        data = json.dumps({
            'email': 'test@email.com',
            'password': 'test'
        })
        res = self.client.post(
            '/api/auth/login',
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(STATUS_UNAUTHORIZED, res.status_code)

    @patch('backend.model.user.User.verify_password')
    def test_login_when_invalid_password(self, mock_verify_password):
        mock_verify_password.return_value = False
        data = json.dumps({
            'email': 'test@email.com',
            'password': 'test'
        })
        res = self.client.post(
            '/api/auth/login',
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(STATUS_UNAUTHORIZED, res.status_code)

    @patch('backend.mapper.auth.AuthMapper.get_logged_in_user_token')
    def test_login_when_logged_in_token(self, mock_get_logged_in_user_token):
        mock_get_logged_in_user_token.return_value = 'test_token'
        data = json.dumps({
            'email': 'test@email.com',
            'password': 'test'
        })
        res = self.client.post(
            '/api/auth/login',
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_OK, res.status_code)
        self.assertEqual('test_token', body['data']['token'])

    def test_login_when_request_is_null(self):
        res = self.client.post(
            '/api/auth/login',
            content_type=self.CONTENT_TYPE,
            data=None
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_login_when_request_is_empty_data(self):
        res = self.client.post(
            '/api/auth/login',
            content_type=self.CONTENT_TYPE,
            data={}
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_login_when_post_invalid_field(self):
        data = (
            {'email': 'test@email.com', 'ham': 'spam'},
            {'hoge': 'hoge@email.com', 'password': 'test'},
            {'hoge': 'hoge@email.com', 'huga': 'test'}
        )
        for d in data:
            res = self.client.post(
                '/api/auth/login',
                content_type=self.CONTENT_TYPE,
                data=json.dumps(d)
            )
            self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

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
            data=json.dumps({})
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_logout_when_post_invalid_field(self):
        res = self.client.post(
            '/api/auth/logout',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'hoge': 'fuga'})
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

    @patch('backend.mapper.auth.AuthMapper.dispose_token')
    @patch('backend.mapper.auth.AuthMapper.generate_auth_token')
    @patch('backend.mapper.auth.AuthMapper.find_by_token')
    @patch('backend.mapper.black_list.BlackListMapper.token_in_black_list')
    def test_reflesh_success(self,
                             mock_token_in_black_list,
                             mock_find_by_token,
                             mock_generate_auth_token,
                             mock_dispose_token):
        mock_token_in_black_list.return_value = False
        mock_find_by_token.return_value = User(
            1, 'test', 'test@email.com', 'test'
        )
        mock_generate_auth_token.return_value = 'test'
        mock_dispose_token.return_value = True
        res = self.client.post(
            '/api/auth/reflesh',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'token': 'test_token'})
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_OK, res.status_code)
        self.assertEqual('test', body['data']['token'])

    def test_reflesh_when_request_is_null(self):
        res = self.client.post(
            '/api/auth/reflesh',
            content_type=self.CONTENT_TYPE,
            data=None
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_reflesh_when_post_empty_data(self):
        res = self.client.post(
            '/api/auth/reflesh',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({})
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_reflesh_when_post_invalid_field(self):
        res = self.client.post(
            '/api/auth/reflesh',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'hoge': 'test_token'})
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)
        self.assertEqual('Request data has invalid fields', body['message'])

    @patch('backend.mapper.black_list.BlackListMapper.token_in_black_list')
    def test_reflesh_when_post_token_in_black_list(self,
                                                   mock_token_in_black_list):
        mock_token_in_black_list.return_value = True
        res = self.client.post(
            '/api/auth/reflesh',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'token': 'test_token'})
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)
        self.assertEqual('Token in blacklist', body['message'])

    @patch('backend.mapper.auth.AuthMapper.find_by_token')
    def test_reflesh_when_post_not_logged_in_token(self, mock_find_by_token):
        mock_find_by_token.return_value = None
        res = self.client.post(
            '/api/auth/reflesh',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'token': 'test_token'})
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)
        self.assertEqual('Invalid token', body['message'])

    @patch('backend.mapper.auth.AuthMapper.generate_auth_token')
    @patch('backend.mapper.auth.AuthMapper.find_by_token')
    def test_reflesh_when_generate_token_failure(self,
                                                 mock_find_by_token,
                                                 mock_generate_auth_token):
        mock_find_by_token.return_value = User(
            1, 'test', 'test@email.com', 'test'
        )
        mock_generate_auth_token.return_value = ''
        res = self.client.post(
            '/api/auth/reflesh',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'token': 'test_token'})
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_INTERNAL_SERVER_ERROR, res.status_code)
        self.assertEqual('Failed publish token', body['message'])

    @patch('backend.mapper.auth.AuthMapper.dispose_token')
    @patch('backend.mapper.auth.AuthMapper.generate_auth_token')
    @patch('backend.mapper.auth.AuthMapper.find_by_token')
    @patch('backend.mapper.black_list.BlackListMapper.token_in_black_list')
    def test_reflesh_when_dispose_token_failure(self,
                                                mock_token_in_black_list,
                                                mock_find_by_token,
                                                mock_generate_auth_token,
                                                mock_dispose_token):
        mock_token_in_black_list.return_value = False
        mock_find_by_token.return_value = User(
            1, 'test', 'test@email.com', 'test'
        )
        mock_generate_auth_token.return_value = 'test'
        mock_dispose_token.return_value = False
        res = self.client.post(
            '/api/auth/reflesh',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({'token': 'test_token'})
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_INTERNAL_SERVER_ERROR, res.status_code)
        self.assertEqual('Failed dispose token', body['message'])
