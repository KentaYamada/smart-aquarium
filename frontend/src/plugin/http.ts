/**
 * http.ts
 * See: https://github.com/axios/axios
 */
import axios, {
    AxiosError,
    AxiosRequestConfig,
    AxiosResponse,
} from 'axios';


// Set config if you need
const config: AxiosRequestConfig = {
    responseType: 'json',
};

const http = axios.create(config);

// setting interceptors if use
http.interceptors.response.use(
    (response: AxiosResponse<any>) => {
        // Do something with response data if you need
        return response;
    },
    (error: AxiosError<any>) => {
        // Do something with response error if you need
        return Promise.reject(error);
    },
);

export default http;
