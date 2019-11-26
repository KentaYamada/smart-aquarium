import { MutationTree } from 'vuex';
import { User } from '@/entity/user';
import { UserState } from '@/store/user';
import { SET_USERS } from '@/store/constant';


const mutations: MutationTree<UserState> = {
    [SET_USERS]: (state: UserState, users: User[]): void => {
        state.users = users;
    },
};

export default mutations;

