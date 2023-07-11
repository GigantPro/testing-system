<script setup>
const headers = useRequestHeaders()
const { data: user_data } = await useFetch(
    "http://backend:5001/user/self/who_am_i",
    { headers: headers, server: true }
);
const user_value = user_data.value;

const router = useRouter()
</script>

<template>
    <nav class="navbar navbar-expand-lg rounded navbar-dark bg-dark text-white shadow" height="70">
        <div class="container-fluid">
            <div class="col-2 ms-2">
                <a class="navbar-brand  align-items-center  text-decoration-none" href="/">
                    <img src="~/assets/brand.png" alt="Education" class="d-inline-block align-text-top rounded"
                        height="50" />
                </a>
            </div>

            <div class="collapse navbar-collapse col-10" id="navbarNav">

                <ul class="nav col-lg-9 d-flex justify-content-center text-center">
                    <li>
                        <a class="nav-link" aria-current="page" href="/">На главную</a>
                    </li>
                    <li>
                        <a class="nav-link" aria-current="page" href="/courses/list">Курсы</a>
                    </li>
                    <li>
                        <a class="nav-link" aria-current="page" href="/me/stats">Успеваемость</a>
                    </li>
                    <li>
                        <a class="nav-link" aria-current="page" href="/user/courses">Учеба</a>
                    </li>
                    <li>
                        <a class="nav-link" aria-current="page" href="/courses/create">Создать свой курс
                        </a>
                    </li>
                </ul>

                <div v-if="user_value" class="col-lg-3 d-flex justify-content-end">
                    <div class="dropdown text-white me-3">
                        <a class="d-block link-light text-decoration-none dropdown-toggle" href="#"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <img class="rounded-circle" :src="user_value.ico_url" alt="ico" height="40" />
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end dropdown-menu-dark">
                            <li>
                                <a class="dropdown-item" :href="'/@' + user_value.username">Мой профиль</a>
                            </li>
                            <li>
                                <a class="dropdown-item" href="/user/settings">Настройки</a>
                            </li>
                            <li>
                                <a class="dropdown-item" href="/user/courses">Мои курсы</a>
                            </li>
                            <li>
                                <a class="dropdown-item disabled" href="#">Мои классы</a>
                            </li>
                            <li>
                                <hr class="dropdown-divider" />
                            </li>
                            <li>
                                <button class="dropdown-item"
                                    @click="async () => { await useFetch('/api/auth/logout', { server: false, method: 'POST' }); await router.go(); await router.push('/');}">Выйти</button>
                            </li>
                        </ul>
                    </div>
                </div>
                <div v-else class="col-lg-3 text-end d-flex justify-content-end">
                    <a class="btn btn-dark rounded border-white" href="/auth?auth=login">Войти</a>
                    <a class="btn btn-dark rounded border-white me-3" href="/auth?auth=registration">Регистрация
                    </a>
                </div>
            </div>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>

    </nav>
</template>

<style scoped>
.navbar {
    margin: 0.3rem 0.6rem 1rem 0.6rem;
}

a {
    color: white;
}

a:hover,
a:active,
a:link,
a:focus-visible,
a:focus {
    color: #53774B;
}
</style>
