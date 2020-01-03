import { GetterTree } from 'vuex';
import { ChartData } from 'chart.js';
import { AquariumWaterQualityState } from '@/store/aquarium-water-quality';
import { RootState } from '@/store/state_type';
import {
    GET_PH_GRAPH_DATA,
    GET_TEMPERATURE_GRAPH_DATA,
    HAS_ITEMS,
} from '@/store/constant';

const getters: GetterTree<AquariumWaterQualityState, RootState> = {
    [HAS_ITEMS]: (state: AquariumWaterQualityState): boolean => {
        // return state.water_qualities.length > 0;
        return true;
    },
    [GET_PH_GRAPH_DATA]: (state: AquariumWaterQualityState): ChartData => {
        const data: ChartData = {
            labels: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
            ],
            datasets: [{
                label: 'pHデータ',
                data: [10, 20, 50, 30, 20, 40],
                borderColor: '#CFD8DC',
                fill: false,
                type: 'line',
                lineTension: 0.3,
            }],
        };

        return data;
    },
    [GET_TEMPERATURE_GRAPH_DATA]: (state: AquariumWaterQualityState): ChartData => {
        const data: ChartData = {
            labels: [
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
            ],
            datasets: [{
                label: '水温データ',
                data: [10, 20, 50, 30, 20, 40],
                borderColor: '#CFD8DC',
                fill: false,
                type: 'line',
                lineTension: 0.3,
            }],
        };

        return data;
    },
};

export default getters;
