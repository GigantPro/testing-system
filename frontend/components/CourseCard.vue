<script setup>
const props = defineProps(['item_'])
</script>

<template>
    <div v-if="props.item_" class="card text-center justifycontent-center">
        <img :src="props.item_.ico_url" class="card-img-top rounded mx-auto d-block" alt="Картинка">
        <div class="card-body">
            <h5 class="card-title">{{ item_.title }}</h5>
            <p class="card-text">{{ item_.description }}</p>
            <NuxtLink :to="'/courses/' + item_.id" class="btn text-white btn-secondary">Перейти к курсу</NuxtLink>
        </div>
    </div>
    <div v-else class="card text-center justifycontent-center">
        <img src="~/assets/loading-screen-cat.gif" class="card-img-top" alt="Картинка">
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
            <a class="btn disabled placeholder col-6 text-white btn-secondary"></a>
        </div>
    </div>
</template>

<style scoped>
.card {
    background-color: #53774B;
    color: #fff;
}
</style>
