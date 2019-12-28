import unittest
from backend.mapper.configuration import ConfigurationMapper
from backend.model.configuration import Configuration


class TestConfigurationMapper(unittest.TestCase):
    def test_find(self):
        data = ConfigurationMapper.find()
        self.assertIsNotNone(data)
        self.assertTrue(isinstance(data, Configuration))

    def test_save(self):
        data = Configuration(6.1, 6.8, 22.8, 24.2, 5)
        result = ConfigurationMapper.save(data)
        self.assertTrue(result)
