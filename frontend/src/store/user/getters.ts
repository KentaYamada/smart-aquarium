import _ from 'lodash';
import { GetterTree } from 'vuex';
import { User } from '@/entity/user';
import { UserState } from '@/store/user';
import { FIND_OR_CREATE, HAS_ITEMS } from '@/store/constant';
import { RootState } from '@/store/state_type';


const getters: GetterTree<UserState, RootState> = {
    [FIND_OR_CREATE]: (state: UserState) => (id?: number): User => {
        if (_.isNil(id)) {
            return new User();
        }

        const user = _.find(state.users, (user: User) => {
            return user.id === id;
        });

        return _.isUndefined(user) ? new User() : user;
    },
    [HAS_ITEMS]: (state: UserState): boolean => {
        return state.users.length > 0;
    },
};

export default getters;

