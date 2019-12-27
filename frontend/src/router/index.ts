import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '@/store';
import Top from '@/views/top/Top.vue';


Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'top',
        component: Top,
    },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
