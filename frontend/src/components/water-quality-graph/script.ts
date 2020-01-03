import { PropType } from 'vue';
import { ChartData, ChartOptions } from 'chart.js';
import { Line } from 'vue-chartjs';

export default {
    extends: Line,
    name: 'water-quality-graph',
    props: {
        chartData: {
            required: false,
            type: Object as PropType<ChartData>,
        },
        chartOptions: {
            required: true,
            type: Object as PropType<ChartOptions>,
        },
    },
    mounted() {
        this.renderChart(this.chartData, this.chartOptions);
    },
};
