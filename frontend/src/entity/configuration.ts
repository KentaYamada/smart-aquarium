/**
 * Configuration entity
 */
export default class Configuration {
    public ph_lower_limit: number;
    public ph_upper_limit: number;
    public temperature_lower_limit: number;
    public temperature_upper_limit: number;
    public measurement_trials: number;

    constructor(
        ph_lower_limit: number = 0.0,
        ph_upper_limit: number = 0.0,
        temperature_lower_limit: number = 0.0,
        temperature_upper_limit: number = 0.0,
        measurement_trials: number = 0
    ) {
        this.ph_lower_limit = ph_lower_limit;
        this.ph_upper_limit = ph_upper_limit;
        this.temperature_lower_limit = temperature_lower_limit;
        this.temperature_upper_limit = temperature_upper_limit;
        this.measurement_trials = measurement_trials;
    }
}
