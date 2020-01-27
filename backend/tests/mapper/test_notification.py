import sqlite3
import unittest
from datetime import datetime
from backend.config import get_config_by_env
from backend.mapper.notification import NotificationMapper
from backend.model.notification import Notification


class TestNotificationMapper(unittest.TestCase):
    def tearDown(self):
        query = "DELETE FROM notifications;"
        db_config = get_config_by_env().get_database_path()
        with sqlite3.connect(db_config, isolation_level='EXCLUSIVE') as tran:
            tran.execute(query)

    def test_save_succeed(self):
        today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = Notification(today, 'test')
        result = NotificationMapper.save(data)
        self.assertTrue(result)

    def test_save_failure_when_pass_null_value(self):
        with self.assertRaises(ValueError):
            NotificationMapper.save(None)

    def test_save_failure_when_invalid_data_type(self):
        with self.assertRaises(TypeError):
            NotificationMapper.save('')
            NotificationMapper.save(1)
            NotificationMapper.save(True)
            NotificationMapper.save([])
