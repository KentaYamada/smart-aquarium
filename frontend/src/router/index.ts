import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '@/store';
import LoginForm from '@/views/login/LoginForm.vue';
import Top from '@/views/top/Top.vue';
import UserList from '@/views/user/list/UserList.vue';


Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'top',
        component: Top,
        meta: {
            requireAuth: true,
        },
    },
    {
        path: '/users',
        name: 'user',
        component: UserList,
        meta: {
            requireAuth: true,
        },
    },
    {
        path: '/login',
        name: 'login',
        component: LoginForm,
    },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireAuth)) {
        const isLoggedIn: boolean = store.getters['auth/isLoggedIn'];
        if (isLoggedIn) {
            next();
        } else {
            next('/login');
        }
    } else {
        next();
    }
});

export default router;
