import Vue from 'vue';
import { mapGetters, mapActions } from 'vuex';
import { ToastConfig } from 'buefy/types/components';
import { NAVIGATIONS } from '@/store/constant';


export default Vue.extend({
    template: '<navigation/>',
    data() {
        return {
            isShowNavi: false,
        };
    },
    computed: {
        ...mapGetters('navigation', [
            NAVIGATIONS,
        ]),
    },
    methods: {
        handleToggleNavi(): void {
            this.isShowNavi = !this.isShowNavi;
        },
        handleCloseNavi(): void {
            this.isShowNavi = false;
        },
    },
});

