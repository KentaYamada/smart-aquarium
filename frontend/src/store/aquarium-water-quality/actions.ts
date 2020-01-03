import { ActionTree } from 'vuex';
import { AxiosResponse } from 'axios';
import http from '@/plugin/http';
import AquariumWaterQuality from '@/entity/aquarium-water-quality';
import { FETCH, SET_AQUARIUM_WATER_QUARITIES } from '@/store/constant';
import { AquariumWaterQualityState } from '@/store/aquarium-water-quality';
import { RootState } from '@/store/state_type';

const ROOT_URL: string = '/api/aquarium_water_qualities/';

const actions: ActionTree<AquariumWaterQualityState, RootState> = {
    [FETCH]: async ({ commit }) => {
        return await http.get(ROOT_URL).then((response: AxiosResponse) => {
            commit(SET_AQUARIUM_WATER_QUARITIES, response.data.aquarium_water_qualities);
        });
    },
};

export default actions;
