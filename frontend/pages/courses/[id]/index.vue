<script setup>
const route = useRoute()
</script>

<template>
    <h1>Курс с id == {{ route.params.id }}</h1>
</template>