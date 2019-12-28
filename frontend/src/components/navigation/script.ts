import Vue from 'vue';
import {
    mapActions,
    mapGetters,
    mapState,
} from 'vuex';
import { ToastConfig } from 'buefy/types/components';
import {
    FETCH,
    HAS_ITEMS,
    NAVIGATIONS
} from '@/store/constant';


export default Vue.extend({
    template: '<navigation/>',
    data() {
        return {
            isShowNavi: false,
        };
    },
    mounted() {
        this.fetch();
    },
    computed: {
        ...mapGetters('navigation', [
            NAVIGATIONS,
        ]),
        ...mapGetters('notification', [
            HAS_ITEMS,
        ]),
        ...mapState('notification', [
            'notifications',
        ]),
    },
    methods: {
        ...mapActions('notification', [
            FETCH,
        ]),
        handleToggleNavi(): void {
            this.isShowNavi = !this.isShowNavi;
        },
        handleCloseNavi(): void {
            this.isShowNavi = false;
        },
    },
});

