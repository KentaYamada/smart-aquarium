import { MutationTree } from 'vuex';
import { Auth } from '@/entity/auth';
import { AuthState } from '@/store/auth';
import { INITIALIZE, SET_TOKEN } from '@/store/constant';

const mutations: MutationTree<AuthState> = {
    [INITIALIZE]: (state: AuthState): void => {
        state.auth = new Auth();
    },
    [SET_TOKEN]: (state: AuthState, token: string): void => {
        state.auth.token = token;
    },
};

export default mutations;

