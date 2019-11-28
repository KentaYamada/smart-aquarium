<template>
    <section class="section">
        <navigation/>
        <div class="container">
            <router-view/>
        </div>
    </section>
</template>

<style scoped lang="scss">
.container {
    margin-top: 20px;
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
