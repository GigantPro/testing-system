<template>
    <nav class="navbar navbar-expand-lg rounded navbar-dark bg-dark">
        <div class="container-fluid">
            <NuxtLink class="navbar-brand" to="/">
                <img src="/favicon.ico" alt="Education"
                    class="d-inline-block align-text-top rounded">
            </NuxtLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav m-auto mb-2 mb-lg-0">
                    <li class="nav-item text-light">
                        <NuxtLink class="nav-link active" aria-current="page" to="/">На главную</NuxtLink>
                    </li>
                    <li class="nav-item text-light">
                        <NuxtLink class="nav-link active" aria-current="page" to="/courses/list">Курсы</NuxtLink>
                    </li>
                    <li class="nav-item text-light">
                        <NuxtLink class="nav-link active" aria-current="page" to="/me/stats">Успеваемость</NuxtLink>
                    </li>
                    <li class="nav-item text-light">
                        <NuxtLink class="nav-link active" aria-current="page" to="/menu">Меню</NuxtLink>
                    </li>
                    <li class="nav-item text-light">
                        <NuxtLink class="nav-link active" aria-current="page" to="/courses/create">Создать свой курс</NuxtLink>
                    </li>
                </ul>

                <button type="button" class="btn btn-dark rounded border-white" @click="onPushedLoginButton">Войти</button>
            </div>

        </div>
    </nav>
</template>

<style scoped>
.navbar {
    margin: .3rem .6rem 1rem .6rem;
}
</style>

<script setup>

const onPushedLoginButton = (e) => {
    console.log(e);
}

</script>
