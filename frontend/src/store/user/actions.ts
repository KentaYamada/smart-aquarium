import { ActionTree } from 'vuex';
import _ from 'lodash';
import http from '@/plugin/http';
import { httpResponse } from 'axios';
import { User, UserSearchOption } from '@/entity/user';
import { UserState } from '@/store/user';
import { RootState } from '@/store/state_type';
import { FETCH, SAVE, DELETE, SET_USERS } from '@/store/constant';


const ROOT_URL: string = '/api/users/';

const actions: ActionTree<UserState, RootState> = {
    [FETCH]: async ({ commit }, option: UserSearchOption) => {
        return await http
            .get(ROOT_URL, { params: option })
            .then((response: httpResponse<any>) => {
                commit(SET_USERS, response.data.users);
            });
    },
    [SAVE]: async ({ commit }, user: User) => {
        let promise$ = null;

        if (_.isNull(user.id)) {
            promise$ = http.post(ROOT_URL, user);
        } else {
            promise$ = http.put(`${ROOT_URL}${user.id}`, user);
        }

        return await promise$;
    },
    [DELETE]: async ({ commit }, id: number) => {
        const url: string = `${ROOT_URL}${id}`;
        return await http.delete(url);
    },
};

export default actions;

