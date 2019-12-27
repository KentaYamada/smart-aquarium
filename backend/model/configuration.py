class Configuration:
    def __init__(
        self,
        id,
        ph_lower_limit,
        ph_upper_limit,
        temperature_lower_limit,
        temperature_upper_limit,
        measurement_trials
    ):
        self.id = id
        self.ph_lower_limit = ph_lower_limit
        self.ph_upper_limit = ph_upper_limit
        self.temperature_lower_limit = temperature_lower_limit
        self.temperature_upper_limit = temperature_upper_limit
        self.measurement_trials = measurement_trials
