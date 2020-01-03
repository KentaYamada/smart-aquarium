export default class AquariumWaterQuality {
    public measured_at: Date;
    public ph: number;
    public temperature: number;

    constructor(measured_at: Date, ph: number, temperature: number) {
        this.measured_at = measured_at;
        this.ph = ph;
        this.temperature = temperature;
    }
}
