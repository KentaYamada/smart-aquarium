import { Module } from 'vuex';
import { User } from '@/entity/user';
import { RootState } from '@/store/state_type';
import actions from './actions';
import getters from './getters';
import mutations from './mutations';


export interface UserState {
    users: User[];
}

const state: UserState = {
    users: [],
};

const namespaced: boolean = true;
const modules: Module<UserState, RootState> = {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};

export default modules;

