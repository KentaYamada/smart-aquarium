import { Module } from 'vuex';
import AquariumWaterQuality from '@/entity/aquarium-water-quality';
import { RootState } from '@/store/state_type';
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

export interface AquariumWaterQualityState {
    water_qualities: AquariumWaterQuality[];
}

const state: AquariumWaterQualityState = {
    water_qualities: [],
};

const namespaced: boolean = true;
const modules: Module<AquariumWaterQualityState, RootState> = {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};

export default modules;
