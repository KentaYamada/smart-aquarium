import { Line } from 'vue-chartjs';

export default {
    extends: Line,
    name: 'water-quality-graph',
    data() {
        const data = {
            labels: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
            ],
            datasets: [{
                label: 'Line dataset',
                data: [10, 20, 50, 30, 20, 40],
                borderColor: '#CFD8DC',
                fill: false,
                type: 'line',
                lineTenstion: 0.3,
            }],
        };

        const options = {
            scales: {
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Month',
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

        return { data, options };
    },
    // props: ['chartData', 'chartOption'],
    mounted() {
        this.renderChart(this.data, this.options);
    },
};
