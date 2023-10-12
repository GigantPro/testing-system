<script setup>
definePageMeta({
  middleware: 'teachers-only'
})

useHead({
    title: 'О курсе | Xiver education',
})


const route = useRoute()

const base_url = '/courses/' + route.params.id + '/edit'

const { data: course_data } = await useAsyncData(
    'course_data_' + route.params.id,
    () => {
        const headers = useRequestHeaders()

        let api_url = ''
        if (process.server) api_url = process.env.SSR_API_BASE_URL + "/course/get/"
        else api_url = "/api/course/get/"

        api_url = api_url + route.params.id

        return $fetch( 
            api_url,
            { headers: headers},
        )
    },
);
</script>

<template>
    <div>
        <h1 class="text-center mt-5 mb-5">Описание курса</h1>
        <div class="container align-items-center justify-content-center items-center">
            <div class="row">
                <div class="col-3 rounded shadow btn-group-vertical mr-5 p-2 second-float justify-content-start" role="group"
                    aria-label="Basic checkbox toggle button group">
                    <div class="text-center">
                        <img :src="course_data.ico_url" alt="Course icon" class="rounded-circle mx-auto d-block shadow" width="70%" >
                        <h4 class="pt-4">{{ course_data.title }}</h4>
                    </div>
                    <hr class="rounded" width="100%">
                    <div class="container list-group text-center" width="100%">
                        <NuxtLink class="list-group-item list-group-item-action" :to="base_url + '/general'">Основные</NuxtLink>
                        <NuxtLink class="list-group-item list-group-item-action" :to="base_url + '/lessons'">Содержание</NuxtLink>
                    </div>
                </div>
                <div class="col-9 shadow rounded ml-5 p-3 second-float">
                    <NuxtPage/>
                </div>
            </div>
        </div>
    </div>
</template>
