import axios, {
    AxiosError,
    AxiosInstance,
    AxiosRequestConfig,
    AxiosResponse,
} from 'axios';
import _ from 'lodash';
import store from '@/store';
import router from '@/router';


// HTTP status
const STATUS_UNAUTHORIZED: number = 401;

const baseConfig: AxiosRequestConfig = {
    responseType: 'json',
};
const http: AxiosInstance = axios.create(baseConfig);

const refleshTokenSucceeded = (response: AxiosResponse, error: AxiosError) => {
    const token: string = `Bearer ${response.data.token}`;

    // update Authorization token
    http.defaults.headers.common.Authorization = token;

    // retry original request
    const config = error.config;
    config.headers.Authorization = token;

    http.request(config);
};

http.interceptors.response.use((response: AxiosResponse) => {
    return response;
}, (error: AxiosError) => {
    const res: AxiosResponse<any> = error.response;

    if (res.status === STATUS_UNAUTHORIZED) {
        if (res.data.refleshing) {
            // request reflesh token
            store.dispatch('/auth/refleshToken')
                .then((response: AxiosResponse) => {
                    refleshTokenSucceeded(response, error);
                });
        } else {
            // redirect login
            store.commit('auth/initialize');
            router.push('/login');
        }
    } else {
        return Promise.reject(error);
    }
});

export default http;
