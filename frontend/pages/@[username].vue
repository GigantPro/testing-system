<script setup>
const route = useRoute()
const { data: user_data } = await useAsyncData(
    'username_' + route.params.username,
    () => {
        const headers = useRequestHeaders()

        let api_url = ''
        if (process.server) api_url = process.env.SSR_API_BASE_URL + "/user/username/"  + route.params.username
        else api_url = "/api/user/username/"  + route.params.username
        return $fetch( 
            api_url,
            { headers: headers },
        )
    },
);

useHead({
    title: route.params.username + ' | Xiver education',
})
</script>

<template>
    <div v-if="user_data" class="mt-auto mb-auto ms-5 me-5">
        <div class="text-center" id="userData">
            <img :src="user_data.ico_url" alt="Ico" class="rounded-4 img-thumbnail mx-auto d-block mb-3" width="200">
            <p class="mb-0"><b>{{ user_data.name }} {{ user_data.surname }}</b></p>
            <p>@{{ user_data.username }}</p>
        </div>
        <hr>
        <div class="text-center" id="userStats">Какая-то статистика</div>
    </div>
    <div v-else class="mt-auto mb-auto ms-5 me-5">
        <div class="text-center text-danger" id="userData">
            <h1>Пользлвателя с именем {{ route.params.username }} не существует!</h1>
        </div>
    </div>
</template>