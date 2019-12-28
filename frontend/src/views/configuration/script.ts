import Vue from 'vue';
import { mapActions, mapState } from 'vuex';
import { AxiosError, AxiosResponse } from 'axios';
import Configuration from '@/entity/configuration';
import { FETCH } from '@/store/constant';
import { ConfigurationForm } from '@/components/configuration-form/ConfigurationForm.vue';

export default Vue.extend({
    components: {
        ConfigurationForm,
    },
    data() {
        return {
            errors: {}
        };
    },
    mounted() {
        this.fetch();
    },
    compouted: {
        ...mapState('configuration', [
            'config',
        ]),
    },
    methods: {
        ...mapActions('configuration', [
            FETCH,
        ]),
    },
});
