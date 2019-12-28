import { MutationTree } from 'vuex';
import _ from 'lodash';
import Notification from '@/entity/notification';
import { NotificationState } from '@/store/notification';
import { SET_NOTIFICATIONS } from '@/store/constant';

const mutations: MutationTree<NotificationState> = {
    [SET_NOTIFICATIONS]: (state: NotificationState, notifications: Notification[]) => {
        state.notifications = _.map(notifications, (item: Notification) => {
            return new Notification(item.created_at, item.message);
        });
    },
};

export default mutations;
