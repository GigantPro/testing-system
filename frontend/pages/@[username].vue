<script setup>
const route = useRoute()

const headers = useRequestHeaders()
const { data: user_data } = await useFetch(
    "http://backend:5001/user/self/who_am_i",
    { headers: headers, server: true }
);
const user_value = user_data.value;
</script>

<template>
    <div class="mt-auto mb-auto ms-5 me-5">
        <div class="text-center" id="userData">
            <img :src="user_value.ico_url" alt="Ico" class="rounded-4 img-thumbnail mx-auto d-block mb-3" width="200">
            <p class="mb-0"><b>{{ user_value.name }} {{ user_value.surname }}</b></p>
            <p>@{{ user_value.username }}</p>
        </div>
        <hr>
        <div class="text-center" id="userStats">Какая-то статистика</div>
    </div>
</template>