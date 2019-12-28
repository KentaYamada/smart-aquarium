import Vue from 'vue';
import Vuex from 'vuex';
import navigation from '@/store/navigation';
import notification from '@/store/notification';
import user from '@/store/user';


Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        navigation,
        notification,
        user,
    },
});

