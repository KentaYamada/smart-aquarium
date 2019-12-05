import { Module } from 'vuex';
import { RootState } from '@/store/state_type';
import getters from './getters';


export interface Navigation {
    title: string;
    icon: string;
    submenu: Navigation[];
}

export interface NavigationState {
    navigations: Navigation[];
}

const state: Navigation = {
    navigations: [
        {
            title: '設定',
            icon: 'fa-user-cog',
            submenu: [
                {
                    title: 'ユーザー',
                    icon: 'fa-user',
                    url: '/users',
                },
            ],
        }
    ] as Navigation[],
};

const namespaced: boolean = true;
const modules: Module<NavigationState, RootState> = {
    namespaced,
    state,
    getters,
};

export default modules;

