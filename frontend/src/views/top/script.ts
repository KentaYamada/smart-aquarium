import Vue from 'vue';
import { mapActions, mapGetters } from 'vuex';
import { ChartOptions } from 'chart.js';
import WaterQualityGraph from '@/components/water-quality-graph/WaterQualityGraph.vue';
import WaterQualityMonitorSearchOption from '@/entity/water-quality-monitor-search-option';
import {
    FETCH,
    GET_PH_GRAPH_DATA,
    GET_TEMPERATURE_GRAPH_DATA,
    HAS_ITEMS
} from '@/store/constant';

export default Vue.extend({
    components: {
        WaterQualityGraph,
    },
    data() {
        return {
            isLoading: false,
            phGraphOptions: this._getPhGraphOptions(),
            temperatureGraphOptions: this._getTemperatureOptions(),
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
            GET_PH_GRAPH_DATA,
            GET_TEMPERATURE_GRAPH_DATA,
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
        /**
         * pH計測グラフオプション取得
         */
        _getPhGraphOptions(): ChartOptions {
            const options: ChartOptions = {
                scales: {
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'pH',
                        },
                    }],
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            stepSize: 10,
                        },
                    }],
                },
            };

            return options;
        },
        /**
         * 水温計測グラフオプション取得
         */
        _getTemperatureOptions(): ChartOptions {
            const options: ChartOptions = {
                scales: {
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: '水温',
                        },
                    }],
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            stepSize: 10,
                        },
                    }],
                },
            };

            return options;
        },
    },
});

