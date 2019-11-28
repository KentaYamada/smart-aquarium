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
            isShowNavi: false,
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
            this.isShowNavi = !this.isShowNavi;
        },
        handleCloseNavi(): void {
            this.isShowNavi = false;
        },
        handleLogout(): void {
            this.logout()
                .then(() => {
                    this._logoutSucceeded();
                })
                .catch(() => {
                    this._logoutFailure();
                });
        },
        _logoutSucceeded(): void {
            const config: ToastConfig = {
                message: 'ログアウトしました',
                type: 'is-success',
            };
            this.$buefy.toast.open(config);
            this.$router.push('/login');
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

