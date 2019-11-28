
import { Module } from 'vuex';
import { Auth } from '@/entity/auth';
import { RootState } from '@/store/state_type';
import actions from './actions';
import getters from './getters';
import mutations from './mutations';


export interface AuthState {
    auth: Auth;
}

const state: AuthState = {
    auth: new Auth(),
};

const namespaced: boolean = true;
const modules: Module<AuthState, RootState> = {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};

export default modules;

