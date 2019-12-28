import { MutationTree } from 'vuex';
import Configuration from '@/entity/configuration';
import { ConfigurationState } from '@/store/configuration';
import { SET_CONFIGURATION } from '@/store/constant';

const mutations: MutationTree<ConfigurationState> = {
    [SET_CONFIGURATION]: (state: ConfigurationState, data: Configuration): void => {
        state.config = new Configuration(
            data.ph_lower_limit,
            data.ph_upper_limit,
            data.temperature_lower_limit,
            data.temperature_upper_limit,
            data.measurement_trials,
        );
    },
};

export default mutations;
