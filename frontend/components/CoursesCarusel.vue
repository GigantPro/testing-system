<script setup>
const { data: top_of_courses, pending, error } = await useAsyncData(
    'most_popular',
    () => {
        const headers = useRequestHeaders()

        let api_url = ''
        if (process.server) api_url = process.env.SSR_API_BASE_URL + "/course/most_popular"
        else api_url = "/api/course/most_popular"
        return $fetch( 
            api_url,
            { headers: headers },
        )
    },
);
</script>

<template>
    <div class="container text-center">
        <div v-if="top_of_courses" class="row align-items-center justify-center justify-content-center">
            <div v-for="item of top_of_courses" :key="item" class="col-xxl-2 col-xl-2 col-lg-3 col-md-4 col-sm-6">
                <CourseCard :item_="item" />
            </div>
            <div class="card more-courses-card col-xxl-2 col-xl-2 col-lg-3 col-md-4 col-sm-6" style="height: 100%;">
                <div class="card-body">
                    <NuxtLink to="/courses" class="btn btn-secondary text-white" style="height: 100%;">Больше
                        курсов</NuxtLink>
                </div>
            </div>
        </div>
        <div v-else-if="pending" class="row align-items-center justify-center justify-content-center">
            <div v-for="index in 10" :key="index" class="col-xxl-2 col-xl-2 col-lg-3 col-md-4 col-sm-6">
                <CourseCard />
            </div>
        </div>
        <div v-else class="card-group text-center align-items-center justify-content-center">
            <h5 class="display-7 text-danger">Ошибка загрузки {{ error }}</h5>
        </div>
    </div>
</template>

<style scoped>
.more-courses-card {
    background-color: #53774B;
}
</style>
