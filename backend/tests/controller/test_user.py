import json
from unittest.mock import patch
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


class TestUserApi(BaseApiTestCase):
    def test_index(self):
        res = self.client.get(
            '/api/users/',
            content_type=self.CONTENT_TYPE
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_OK, res.status_code)
        self.assertEqual(3, len(body['users']))

    @patch('backend.mapper.user.UserMapper.find_users')
    def test_index_when_no_users(self, mock_find_users):
        mock_find_users.return_value = ()
        res = self.client.get(
            '/api/users/',
            content_type=self.CONTENT_TYPE
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_OK, res.status_code)
        self.assertEqual(0, len(body['users']))

    def test_add(self):
        data = json.dumps({
            'id': None,
            'name': 'test',
            'email': 'test@email.com',
            'password': 'secret'
        })
        res = self.client.post(
            '/api/users/',
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_CREATED, res.status_code)
        self.assertTrue(body['result'])

    def test_add_when_post_no_data(self):
        res = self.client.post(
            '/api/users/',
            content_type=self.CONTENT_TYPE,
            data=None
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_add_when_post_empty_data(self):
        res = self.client.post(
            '/api/users/',
            content_type=self.CONTENT_TYPE,
            data=json.dumps({})
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_add_when_post_invalid_fields(self):
        data = json.dumps({
            'ham': None,
            'spam': 'test',
            'egg': 'test@email.com',
            'python': 'secret'
        })
        res = self.client.post(
            '/api/users/',
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    @patch('backend.mapper.user.UserMapper.save')
    def test_add_when_save_failure(self, mock_save):
        mock_save.return_value = False
        data = json.dumps({
            'id': None,
            'name': 'test',
            'email': 'test@email.com',
            'password': 'secret'
        })
        res = self.client.post(
            '/api/users/',
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_CONFLICT, res.status_code)
        self.assertEqual('Failed add data', body['message'])

    def test_edit(self):
        url = urljoin('/api/users/', '1')
        data = json.dumps({
            'id': 1,
            'name': 'test',
            'email': 'test@email.com',
            'password': 'secret'
        })
        res = self.client.put(
            url,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_OK, res.status_code)
        self.assertTrue(body['result'])

    def test_edit_when_query_id_is_null(self):
        data = json.dumps({
            'id': 1,
            'name': 'test',
            'email': 'test@email.com',
            'password': 'secret'
        })
        res = self.client.put(
            '/api/users/',
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(STATUS_METHOD_NOT_ALLOWED, res.status_code)

    def test_edit_when_query_id_is_invalid_value(self):
        url = urljoin('/api/users/', 'test')
        data = json.dumps({
            'id': 1,
            'name': 'test',
            'email': 'test@email.com',
            'password': 'secret'
        })
        res = self.client.put(
            url,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(STATUS_NOT_FOUND, res.status_code)

    def test_edit_when_request_data_is_null(self):
        url = urljoin('/api/users/', '1')
        res = self.client.put(
            url,
            content_type=self.CONTENT_TYPE,
            data=None
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    def test_edit_when_request_data_empty_data(self):
        url = urljoin('/api/users/', '1')
        res = self.client.put(
            url,
            content_type=self.CONTENT_TYPE,
            data=json.dumps({})
        )
        self.assertEqual(STATUS_BAD_REQUEST, res.status_code)

    @patch('backend.mapper.user.UserMapper.exist_user')
    def test_edit_when_request_not_exist_user_data(self, mock_exitst_user):
        mock_exitst_user.return_value = False
        url = urljoin('/api/users/', '1')
        data = json.dumps({
            'id': 1,
            'name': 'test',
            'email': 'test@email.com',
            'password': 'secret'
        })
        res = self.client.put(
            url,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_NOT_FOUND, res.status_code)
        self.assertEqual('Not exist user', body['message'])

    @patch('backend.mapper.user.UserMapper.save')
    def test_edit_when_save_failure(self, mock_save):
        mock_save.return_value = False
        url = urljoin('/api/users/', '1')
        data = json.dumps({
            'id': 1,
            'name': 'test',
            'email': 'test@email.com',
            'password': 'secret'
        })
        res = self.client.put(
            url,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_CONFLICT, res.status_code)
        self.assertEqual('Failed edit data', body['message'])

    def test_delete(self):
        url = urljoin('/api/users/', '1')
        res = self.client.delete(url)
        self.assertEqual(STATUS_NO_CONTENT, res.status_code)

    def test_delete_when_query_id_is_null(self):
        res = self.client.delete('/api/users/')
        self.assertEqual(STATUS_METHOD_NOT_ALLOWED, res.status_code)

    def test_delete_when_query_id_is_invalid_value(self):
        url = urljoin('/api/users/', 'test')
        res = self.client.delete(url)
        self.assertEqual(STATUS_NOT_FOUND, res.status_code)

    @patch('backend.mapper.user.UserMapper.delete')
    def test_delete_when_delete_failure(self, mock_delete):
        mock_delete.return_value = False
        url = urljoin('/api/users/', '1')
        res = self.client.delete(url)
        body = json.loads(res.get_data())
        self.assertEqual(STATUS_NOT_FOUND, res.status_code)
        self.assertEqual('Not exist user', body['message'])
