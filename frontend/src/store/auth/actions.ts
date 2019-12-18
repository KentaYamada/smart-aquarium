import { ActionTree } from 'vuex';
import { AxiosResponse } from 'axios';
import http from '@/plugin/http';
import { Auth } from '@/entity/auth';
import { AuthState } from '@/store/auth';
import { RootState } from '@/store/state_type';
import {
    INITIALIZE,
    LOGIN,
    LOGOUT,
    REFLESH_TOKEN,
    SET_TOKEN,
} from '@/store/constant';

const LOGIN_API_URL: string = '/api/auth/login';
const LOGOUT_API_URL: string = '/api/auth/logout';
const REFLESH_TOKEN_API_URL: string = '/api/auth/reflesh';

const actions: ActionTree<AuthState, RootState> = {
    [LOGIN]: async (context: any): Promise => {
        const auth: Auth = context.state.auth;
        const data = {
            email: auth.email,
            password: auth.password,
        };
        const promise$: Promise = http.post(LOGIN_API_URL, data);

        promise$.then((response: AxiosResponse) => {
            context.commit(SET_TOKEN, response.data.token);
        });

        return await promise$;
    },
    [LOGOUT]: async (context: any): Promise => {
        const token: string = context.state.auth.token;
        const promise$: Promise = http.post(LOGOUT_API_URL, { token });
        promise$.then(() => {
            context.commit(INITIALIZE);
        });

        return await promise$;
    },
    [REFLESH_TOKEN]: async (context: any): Promise => {
        const token: string = context.state.auth.token;
        const promise$: Promise = http.post(REFLESH_TOKEN_API_URL, { token });

        promise$.then((response: AxiosResponse) => {
            context.commit(SET_TOKEN, response.data.token);
        });

        return await promise$;
    },
};

export default actions;

