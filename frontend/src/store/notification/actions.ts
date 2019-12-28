import { ActionTree } from 'vuex';
import http from '@/plugin/http';
import Notification from '@/entity/notification';
import { NotificationState } from '@/store/notification';
import { RootState } from '@/store/state_type';
import { FETCH, SET_NOTIFICATIONS } from '@/store/constant';

const ROOT_URL: string = '/api/notifications/';

const actions: ActionTree<NotificationState, RootState> = {
    [FETCH]: async ({ commit }) => {
        return await http.get(ROOT_URL).then((response: AxiosResponse) => {
            commit(SET_NOTIFICATIONS, response.data.notifications);
        });
    },
};

export default actions;
