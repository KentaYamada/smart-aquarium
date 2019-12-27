<template>
    <div id="app">
        <navigation/>
        <router-view/>
    </div>
</template>

<style scoped lang="scss">
#app {
    background-color: #eee;
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
