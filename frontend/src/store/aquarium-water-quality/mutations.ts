import { MutationTree } from 'vuex';
import _ from 'lodash';
import AquariumWaterQuality from '@/entity/aquarium-water-quality';
import { AquariumWaterQualityState } from '@/store/aquarium-water-quality';
import { SET_AQUARIUM_WATER_QUARITIES } from '@/store/constant';

const mutations: MutationTree<AquariumWaterQualityState> = {
    [SET_AQUARIUM_WATER_QUARITIES]: (state: AquariumWaterQualityState, data: AquariumWaterQuality[]): void => {
        state.aquarium_water_qualities = data;
    },
};

export default mutations;
