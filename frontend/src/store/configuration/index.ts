import { Module } from 'vuex';
import Configuration from '@/entity/configuration';
import { RootState } from '@/store/state_type';
import actions from './actions';
import mutations from './mutations';


export interface ConfigurationState {
    config: Configuration;
}

const state: ConfigurationState = {
    config: new Configuration(),
};

const namespaced: boolean = true;
const modules: Module<ConfigurationState, RootState> = {
    namespaced,
    state,
    actions,
    mutations,
};

export default modules;
