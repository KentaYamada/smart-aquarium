import Vue from 'vue';
import Vuex from 'vuex';
import aquariumWaterQuality from '@/store/aquarium-water-quality';
import configuration from '@/store/configuration';
import navigation from '@/store/navigation';
import notification from '@/store/notification';

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        aquariumWaterQuality,
        configuration,
        navigation,
        notification,
    },
});

