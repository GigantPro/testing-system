<script setup>
const route = useRoute()
</script>

<template>
    <h1>Профиль с username == {{ route.params.username }}</h1>
</template>