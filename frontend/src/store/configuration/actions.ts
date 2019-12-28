import { ActionTree } from 'vuex';
import { AxiosResponse } from 'axios';
import http from '@/plugin/http';
import { FETCH, SAVE, SET_CONFIGURATION } from '@/store/constant';
import Configuration from '@/entity/configuration';
import { ConfigurationState } from '@/store/configuration';
import { RootState } from '@/store/state_type';

const ROOT_URL: string = '/api/configurations/';

const actions: ActionTree<ConfigurationState, RootState> = {
    [FETCH]: async ({ commit }) => {
        return http.get(ROOT_URL).then((response: AxiosResponse) => {
            commit(SET_CONFIGURATION, response.data.configuration);
        });
    },
    [SAVE]: async ({ commit }, configuration: Configuration) => {
        return await http.post(ROOT_URL, configuration);
    },
};

export default actions;
