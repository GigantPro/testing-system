<script setup>
const { data: user_data } = await useAsyncData(
    'who_am_i',
    () => {
        const headers = useRequestHeaders()

        let api_url = ''
        if (process.server) api_url = process.env.SSR_API_BASE_URL + "/user/self/who_am_i"
        else api_url = "/api/user/self/who_am_i"
        return $fetch( 
            api_url,
            { headers: headers },
        )
    },
);
const router = useRouter()

let logged = false
if (user_data.value) logged = true
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
                        <NuxtLink exact no-prefetch class="nav-link" aria-current="page" to="/">На главную</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink exact no-prefetch class="nav-link" aria-current="page" to="/courses">Курсы</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink exact no-prefetch class="nav-link" aria-current="page" to="/me/stats">Успеваемость</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink exact no-prefetch class="nav-link" aria-current="page" to="/user/courses">Учеба</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink exact no-prefetch class="nav-link" aria-current="page" to="/courses/create">Создать свой курс
                        </NuxtLink>
                    </li>
                </ul>

                <div v-if="logged" class="col-lg-3 d-flex justify-content-end">
                    <div class="dropdown text-white me-3">
                        <a class="d-block link-light text-decoration-none dropdown-toggle" href="#"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <img class="rounded-circle" :src="user_data.ico_url" alt="ico" height="40" />
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end dropdown-menu-dark">
                            <li>
                                <NuxtLink exact no-prefetch class="dropdown-item" :to="'/@' + user_data.username">Мой профиль</NuxtLink>
                            </li>
                            <li>
                                <NuxtLink exact no-prefetch class="dropdown-item" to="/user/settings">Настройки</NuxtLink>
                            </li>
                            <li>
                                <NuxtLink exact no-prefetch class="dropdown-item" to="/user/courses">Мои курсы</NuxtLink>
                            </li>
                            <li>
                                <NuxtLink exact no-prefetch class="dropdown-item disabled" to="#">Мои классы</NuxtLink>
                            </li>
                            <li>
                                <hr class="dropdown-divider" />
                            </li>
                            <li>
                                <button class="dropdown-item"
                                    @click="async () => { await useFetch('/api/auth/logout', { server: false, method: 'POST' }); await router.push('/'); await router.go();}">Выйти</button>
                            </li>
                        </ul>
                    </div>
                </div>
                <div v-else class="col-lg-3 text-end d-flex justify-content-end pe-3">
                    <a class="btn rounded border-dark" href="/auth?auth=login" id="loginBtn">Войти</a>
                </div>
            </div>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>

    </nav>
</template>

<style scoped lang="scss">
.navbar {
    margin: 0.3rem 0.6rem 1rem 0.6rem;
}

a:hover,
a:active,
a:focus-visible,
a:focus {
    color: #53774B;
}
a {
    color: white;
}

li {
    margin: auto .9rem auto .9rem;
}

a.dropdown-item:hover {
    color: #77a86c;
}

#loginBtn {
    background-color: #53774B;
}
#loginBtn:hover,
#loginBtn:active,
#loginBtn:link,
#loginBtn:focus-visible,
#loginBtn:focus {
    color: #fff;
    background-color: #486841;
}
</style>
