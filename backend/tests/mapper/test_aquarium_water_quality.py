import unittest
from backend.mapper.aquarium_water_quality import AquariumWaterQualityMapper
from backend.model.aquarium_water_quality import AquariumWaterQualitySearchOption


class TestAquariumWaterQuality(unittest.TestCase):
    def test_find(self):
        # option = AquariumWaterQualitySearchOption()
        data = AquariumWaterQualityMapper.find()
        self.assertIsNotNone(data)
