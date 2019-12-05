import { GetterTree } from 'vuex';
import { Navigation, NavigationState } from '@/store/navigation';
import { NAVIGATIONS } from '@/store/constant';

const getters: GetterTree<NavigationState, RootState> = {
    [NAVIGATIONS]: (state: NavigationState): Navigation[] => {
        return state.navigations;
    },
};

export default getters;
