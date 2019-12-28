import { GetterTree } from 'vuex';
import { NotificationState } from '@/store/user';
import { HAS_ITEMS } from '@/store/constant';
import { RootState } from '@/store/state_type';

const getters: GetterTree<NotificationState, RootState> = {
    [HAS_ITEMS]: (state: NotificationState): boolean => {
        return state.notifications.length > 0;
    },
};

export default getters;
