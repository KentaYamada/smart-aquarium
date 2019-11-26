import _ from 'lodash';
import { GetterTree } from 'vuex';
import { AuthState } from '@/store/auth';
import { RootState } from '@/store/state_type';
import { GET_TOKEN, IS_LOGGED_IN } from '@/store/constant';

const getters: GetterTree<AuthState, RootState> = {
    [GET_TOKEN]: (state: AuthState): string => {
        return state.auth.token;
    },
    [IS_LOGGED_IN]: (state: AuthState): boolean => {
        return !_.isEmpty(state.auth.token);
    },
};

export default getters;

