<script setup>
const props = defineProps(['item_'])
</script>

<template>
    <div v-if="props.item_" class="card">
        <img :src="item_.img_url" class="card-img-top" alt="Картинка">
        <div class="card-body">
            <h5 class="card-title">{{ item_.titel }}</h5>
            <p class="card-text">{{ item_.description }}</p>
            <NuxtLink :to="'/courses/course/' + item_.id" class="btn btn-primary text-white btn-secondary">Перейти к курсу</NuxtLink>
        </div>
    </div>
    <div v-else class="card">
        <img src="https://media.tenor.com/7t8foti8FG8AAAAC/loading-screen-cat.gif" class="card-img-top" alt="Картинка">
        <div class="card-body">
            <h5 class="card-title placeholder-glow">
                <span class="placeholder col-6"></span>
            </h5>
            <p class="card-text placeholder-glow">
                <span class="placeholder col-7"></span>
                <span class="placeholder col-4"></span>
                <span class="placeholder col-4"></span>
                <span class="placeholder col-6"></span>
                <span class="placeholder col-8"></span>
            </p>
            <a class="btn btn-primary disabled placeholder col-6 text-white btn-secondary"></a>
        </div>
    </div>
</template>

<style scoped>
.card {
    background-color: #53774B;
    color: #fff;
}
</style>
