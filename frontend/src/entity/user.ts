/**
 * User entity
 */
export class User {
    public id: number | null;
    public name: string;
    public email: string;
    public password: string;

    constructor(
        id: number | null = null,
        name: string = '',
        email: string = '',
        password: string = '') {
        this.id = id;
        this.name = name;
        this.email = email;
        this.password = password;
    }
}

export class UserSearchOption {
    q: string;
}

