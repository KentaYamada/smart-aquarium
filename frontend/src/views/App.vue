<template>
    <div id="app">
        <navigation/>
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<style scoped lang="scss">
#app {
    background-color: #eee;

    .container {
        margin-top: 20px;
    }
}
</style>

<script lang="ts">
import Vue from 'vue';
import Navigation from '@/components/navigation/Navigation.vue';


export default Vue.extend({
    components: {
        Navigation
    }
});

</script>
