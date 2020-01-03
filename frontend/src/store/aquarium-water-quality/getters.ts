import { GetterTree } from 'vuex';
import { AquariumWaterQualityState } from '@/store/aquarium_water_quality';
import { RootState } from '@/store/state_type';
import { HAS_ITEMS } from '@/store/constant';

const getters: GetterTree<AquariumWaterQualityState, RootState> = {
    [HAS_ITEMS]: (state: AquariumWaterQualityState): boolean => {
        return state.water_qualities.length > 0;
    },
};

export default getters;
