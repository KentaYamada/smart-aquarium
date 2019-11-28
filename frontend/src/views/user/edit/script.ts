import Vue from 'vue';
import _ from 'lodash';
import { mapActions } from 'vuex';
import { AxiosError, AxiosResponse } from 'axios';
import { ToastConfig } from 'buefy/types/components';
import { User } from '@/entity/user';
import { SAVE } from '@/store/constant';
import { SAVE_SUCCESS } from '@/views/constant';


export default Vue.extend({
    props: {
        user: {
            required: true,
            type: User,
        },
    },
    data() {
        return {
            errors: {},
        };
    },
    methods: {
        ...mapActions('user', [
            SAVE,
        ]),
        handleSave(): void {
            this.save(this.user)
                .then((response: AxiosResponse) => {
                    this.$emit('close');
                    this.$emit(SAVE_SUCCESS, response.data.message);
                })
                .catch((error: AxiosError) => {
                    if (!_.isNil(error.response.error)) {
                        this.errors = error.response.error;
                    }

                    const config: ToastConfig = {
                        message: error.response.data.message,
                        type: 'is-danger',
                    };
                    this.$toast.open(config);
                });
        },
    },
});

