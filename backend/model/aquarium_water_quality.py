class AquariumWaterQuality:
    def __init__(self, measured_at, ph, temperature, **kwargs):
        self.measured_at = measured_at
        self.ph = ph
        self.temperature = temperature


class AquariumWaterQualitySearchOption:
    def __init__(self, search_date, hour_from, hour_to, **kwargs):
        self.search_date = search_date
        self.hour_from = hour_from
        self.hour_to = hour_to
