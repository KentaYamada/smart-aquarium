import Vue from 'vue';
import Vuex from 'vuex';
import configuration from '@/store/configuration';
import navigation from '@/store/navigation';
import notification from '@/store/notification';
import user from '@/store/user';


Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        configuration,
        navigation,
        notification,
        user,
    },
});

