import { ActionTree } from 'vuex';
import _ from 'lodash';
import axios, { AxiosResponse } from 'axios';
import { User, UserSearchOption } from '@/entity/user';
import { UserState } from '@/store/user';
import { RootState } from '@/store/state_type';
import { FETCH, SAVE, DELETE, SET_USERS } from '@/store/constant';


const ROOT_URL: string = '/api/users/';

const actions: ActionTree<UserState, RootState> = {
    [FETCH]: async ({ commit }, option: UserSearchOption) => {
        return await axios
            .get(ROOT_URL, { params: option })
            .then((response: AxiosResponse<any>) => {
                commit(SET_USERS, response.data.users);
            });
    },
    [SAVE]: async ({ commit }, user: User) => {
        let promise$ = null;

        if (_.isNull(user.id)) {
            promise$ = axios.post(ROOT_URL, user);
        } else {
            promise$ = axios.put(`${ROOT_URL}${user.id}`, user);
        }

        return await promise$;
    },
    [DELETE]: async ({ commit }, id: number) => {
        const url: string = `${ROOT_URL}${id}`;
        return await axios.delete(url);
    },
};

export default actions;

