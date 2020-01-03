import Vue from 'vue';
import { mapActions, mapGetters } from 'vuex';
import WaterQualityGraph from '@/components/water-quality-graph/WaterQualityGraph.vue';
import WaterQualityMonitorSearchOption from '@/entity/water-quality-monitor-search-option';
import { FETCH, HAS_ITEMS } from '@/store/constant';

export default Vue.extend({
    components: {
        WaterQualityGraph,
    },
    data() {
        return {
            isLoading: false,
        };
    },
    mounted() {
        this.isLoading = true;
        this.fetch()
            .finally(() => {
                this.isLoading = false;
            });
    },
    computed: {
        ...mapGetters('aquariumWaterQuality', [
            HAS_ITEMS,
        ]),
    },
    methods: {
        ...mapActions('aquariumWaterQuality', [
            FETCH,
        ]),
        /**
         * 計測データ検索
         */
        handleClickUpdate(): void {
        },
        /**
         * 検索条件リセット
         */
        handleClickReset(): void {
            this.$data.option.measured_at = null;
            this.$data.option.measured_time_from = null;
            this.$data.option.measured_time_to = null;
        },
    },
});

