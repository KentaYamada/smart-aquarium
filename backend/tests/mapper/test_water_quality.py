import sqlite3
import unittest
from datetime import datetime
from backend.config import get_config_by_env
from backend.model.water_quality import WaterQuality
from backend.mapper.water_quality import WaterQualityMapper


class TestWaterQualityMapper(unittest.TestCase):
    def tearDown(self):
        query = "DELETE FROM water_qualities;"
        db_config = get_config_by_env().get_database_path()
        with sqlite3.connect(db_config, isolation_level='EXCLUSIVE') as tran:
            tran.execute(query)

    def test_save(self):
        today = datetime.now()
        data = WaterQuality(
            today.strftime('%Y-%m-%d'),
            today.strftime('%H:%M:%S'),
            6.8,
            23.2
        )
        result = WaterQualityMapper.save(data)
        self.assertTrue(result)

    def test_save_failure_when_pass_null_value(self):
        with self.assertRaises(ValueError):
            WaterQualityMapper.save(None)

    def test_save_failure_when_invalid_data_type(self):
        with self.assertRaises(TypeError):
            WaterQualityMapper.save('')
            WaterQualityMapper.save(1)
            WaterQualityMapper.save(True)
            WaterQualityMapper.save([])

    def test_save_failure_when_duplicate_data_insertion(self):
        today = datetime.now()
        data = WaterQuality(
            today.strftime('%Y-%m-%d'),
            today.strftime('%H:%M:%S'),
            6.8,
            23.2
        )
        WaterQualityMapper.save(data)

        with self.assertRaises(sqlite3.IntegrityError):
            WaterQualityMapper.save(data)
