<script setup>
useHead({
    title: '404 | Xiver education',
})
</script>


<template>
    <div class="d-flex align-items-center justify-content-center vh-10">
        <div class="text-center">
            <h1 class="display-1 fw-bold">404</h1>
            <p class="fs-3"> <span class="text-danger">Opps!</span> Страница не найдена.</p>
            <p class="lead">
                Похоже, что страницу, которую вы ищите, котик не нашел...
            </p>
            <p class="lead">
                <img src="~/assets/loading-screen-cat.gif" alt="">
            </p>
            <NuxtLink to="/" class="btn btn-primary">Домой</NuxtLink>
        </div>
    </div>
</template>
  