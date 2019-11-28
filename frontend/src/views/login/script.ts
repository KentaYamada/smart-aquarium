import Vue from 'vue'
import { mapActions, mapState } from 'vuex';
import { ToastConfig } from 'buefy/types/components';
import { AxiosError, AxiosResponse } from 'axios';
import { LOGIN } from '@/store/constant';


export default Vue.extend({
    computed: {
        ...mapState('auth', [
            'auth'
        ]),
    },
    methods: {
        ...mapActions('auth', [
            LOGIN,
        ]),
        handleLogin(): void {
            this.login()
                .then((response: AxiosResponse) => {
                    this.$router.push('/');
                })
                .catch((error: AxiosError) => {
                    const config: ToastConfig = {
                        message: 'アプリケーションエラーが発生しました。',
                        type: 'is-danger',
                    };
                    this.$buefy.toast.open(config);
                });
        },
    },
});

