import { Module } from 'vuex';
import Notification from '@/entity/notification';
import { RootState } from '@/store/state_type';
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

export interface NotificationState {
    notifications: Notification[];
}

const state: NotificationState = {
    notifications: [],
};

const namespaced: boolean = true;
const modules: Module<NotificationState, RootState> = {
    namespaced,
    state,
    actions,
    getters,
    mutations,
};

export default modules;
