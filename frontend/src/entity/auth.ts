/**
 * Authorication entity
 */
export class Auth {
    public email: string;
    public password: string;
    public token: string;

    constructor(email: string = '', password: string = '', token = '') {
        this.email = email;
        this.password = password;
        this.token = token;
    }
}

