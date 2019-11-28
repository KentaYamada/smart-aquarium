import unittest
from backend import app


class BaseApiTestCase(unittest.TestCase):
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.endpoint = ''

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
