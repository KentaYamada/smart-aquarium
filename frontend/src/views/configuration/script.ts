import Vue from 'vue';
import { mapActions, mapMutations, mapState } from 'vuex';
import { AxiosError, AxiosResponse } from 'axios';
import _ from 'lodash';
import { ToastConfig } from 'buefy/types/components';
import Configuration from '@/entity/configuration';
import { FETCH, SAVE, SET_CONFIGURATION } from '@/store/constant';

export default Vue.extend({
    data() {
        return {
            config: {},
            errors: {},
        };
    },
    mounted() {
        this.fetch();
        this.config = _.cloneDeep(this.$store.state.configuration.config);
    },
    methods: {
        ...mapActions('configuration', [
            FETCH,
            SAVE,
        ]),
        ...mapMutations('configuration', [
            SET_CONFIGURATION,
        ]),
        handleClickSave(): void {
            this.save(this.config)
                .then((response: AxiosResponse) => {
                    const option: ToastConfig = {
                        message: response.data.message,
                        type: 'is-success',
                    };
                    this.$buefy.toast.open(option);
                    this.fetch();
                })
                .catch(() => {
                    const option: ToastConfig = {
                        message: '保存に失敗しました',
                        type: 'is-danger',
                    };
                    this.$buefy.toast.open(option);
                });
        },
    },
});
