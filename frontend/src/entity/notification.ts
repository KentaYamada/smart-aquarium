/**
 * Notification entity
 */
export default class Notification {
    public created_at: Date;
    public message: string;

    constructor(created_at: Date, message: string) {
        this.created_at = created_at;
        this.message = message;
    }
};
