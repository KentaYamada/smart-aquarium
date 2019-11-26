import Vue from 'vue';
import { mapGetters, mapActions } from 'vuex';
import { ToastConfig } from 'buefy/types/components';
import { IS_LOGGED_IN, LOGOUT } from '@/store/constant';

const navigations = [
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
    },
];

export default Vue.extend({
    template: '<navigation/>',
    data() {
        return {
            navigations,
            isShowNav: false,
        };
    },
    computed: {
        ...mapGetters('auth', [
            IS_LOGGED_IN,
        ]),
    },
    methods: {
        ...mapActions('auth', [
            LOGOUT,
        ]),
        handleToggleNavi(): void {
            this.isShowNav = !this.isShowNav;
        },
        handleLogout(): void {
            this.logout()
                .then(() => {
                    this._logoutSucceeded();
                })
                .cath(() => {
                    this._logoutFailure();
                });
        },
        _logoutSucceeded(): void {
            const config: ToastConfig = {
                message: 'ログアウトしました',
                type: 'is-success',
            };
            this.$buefy.toast.open(config);
        },
        _logoutFailure(): void {
            const config: ToastConfig = {
                message: 'ログアウトに失敗しました',
                type: 'is-danger',
            };
            this.$buefy.toast.open(config);
        },
    },
});

