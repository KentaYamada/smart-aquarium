import _ from 'lodash';
import { MutationTree } from 'vuex';
import { User } from '@/entity/user';
import { UserState } from '@/store/user';
import { SET_USERS } from '@/store/constant';


const mutations: MutationTree<UserState> = {
    [SET_USERS]: (state: UserState, users: User[]): void => {
        state.users = _.map(users, (user: User) => {
            return new User(user.id, user.name, user.email, user.password);
        });
    },
};

export default mutations;

