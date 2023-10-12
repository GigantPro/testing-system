<script setup>
const route = useRoute()
</script>

<template>
    <div>
        <h1>Курс с id == {{ route.params.id }}</h1>
        <NuxtLink :to="'/courses/' + route.params.id + '/edit'" class="btn text-white btn-secondary">Редактировать</NuxtLink>
    </div>
</template>