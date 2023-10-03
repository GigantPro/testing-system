<script setup>
definePageMeta({
  middleware: 'logged-users-only'
})

useHead({
    title: 'Настройки пользователя | Xiver education',
})

const router = useRouter()

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
const user_value = user_data.value;

if (!user_value) {
  router.push("/auth");
}

const messageUnderMail = ref("Пока нет email сервера, поэтому пользователь сразу являются подтвержденными!");
const classMessageUnderMail = ref("text-danger");
const classVefifCode = ref("");

const onProveMailClick = async () => {
    const { data } = await useFetch(
        '/api/user/verification'
    )
    
}
</script>


<template>
  <div class="ms-5 me-5 mb-6">
    <h1 class="text-center mb-5">Настройки</h1>
    <div class="row me-6 ms-6 text-center">
        <div>
            Почта: {{ user_value.email }} <button class="btn btn-dark rounded border-white" @click="onProveMailClick"> Подтвердить</button>
            <p :class="classMessageUnderMail">{{ messageUnderMail.value }}</p>
            <input :class="classVefifCode.value" type="text" placeholder="Введите код из письма на почте" id="verifCode" hidden>
        </div>
    </div>
  </div>
</template>
