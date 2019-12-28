import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '@/store';
import Configuration from '@/views/configuration/Configuration.vue';
import Top from '@/views/top/Top.vue';


Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'top',
        component: Top,
    },
    {
        path: '/configurations',
        name: 'configuration',
        component: Configuration,
    },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
