/**
 * WaterQualityMonitorSearchOption entity
 */
export default class WaterQualityMonitorSearchOption {
    /** 計測日 */
    public measured_at: Date;
    /** 計測時刻(from) */
    public measured_time_from: number;
    /** 計測時刻(to) */
    public measured_time_to: number;

    constructor(
        measured_at: Date,
        measured_time_from: number,
        measured_time_to: number
    ) {
        this.measured_at = measured_at;
        this.measured_time_from = measured_time_from;
        this.measured_time_to = measured_time_to;
    }
}
