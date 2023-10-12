<script setup>
useHead({
    title: 'Курсы | Xiver education',
});

const coursesPlateMsg = ref("");
const selected = ref("popularity")

const pending = ref(true)
const courses = ref(null)

const startIndex = ref(0)
const count = ref(10)

const { data: courses_data } = await useAsyncData(
    'popular_courses' + selected,
    () => {
        const headers = useRequestHeaders()

        let api_url = ''
        if (process.server) api_url = process.env.SSR_API_BASE_URL + "/course/popular_by"
        else api_url = "/api/course/popular_by"
        return $fetch( 
            api_url,
            { headers: headers,
            query: {
                start_index: startIndex.value,
                count: count.value,
                by_: selected.value,
            }},
        )
    },
);

watch(selected, async (selected) => {
    pending.value = true
    const { data: new_courses_data, pending: pp } = useAsyncData(
        'popular_courses_' + selected,
        () => {
            const headers = useRequestHeaders()

            let api_url = ''
            if (process.server) api_url = process.env.SSR_API_BASE_URL + "/course/popular_by"
            else api_url = "/api/course/popular_by"
            return $fetch(
                api_url,
                { headers: headers,
                query: {
                    start_index: startIndex.value,
                    count: count.value,
                    by_: selected,
                }},
            )
        },
    );
    watch(pp, (pp) => {
        if (!pp) {
            courses.value = new_courses_data.value
            pending.value = false
        }
    })
})

if (!courses_data.value) {
    coursesPlateMsg.value = "Нет курсов, удовлетворяющих вашим условиям.";
} else {
    courses.value = courses_data.value
}
pending.value = false
</script>


<template>
    <div>
        <h1 class="text-center mt-5 mb-5">Список курсов</h1>
        <div class="container align-items-center justify-content-center items-center">
            <div class="row">
                <div class="col-2 rounded shadow btn-group-vertical mr-5 p-2 second-float justify-content-start" role="group"
                    aria-label="Basic checkbox toggle button group">
                    <h4 class="mb-3">Фильтры</h4>

                    <div>
                        <h5>Фильтровать по</h5>
                        <select class="form-select form-select-sm text-wrap" aria-label="Фильтры" v-model="selected">
                            <option value="popularity" selected>Популярности</option>
                            <option value="reviews_count">Отзывам</option>
                            <option value="rating">Рейтингу</option>
                            <option value="passed_count">По кол-ву прошедших</option>
                            <option value="passing_count">По кол-ву проходящих</option>
                            <option value="created_time">Времени создания</option>
                        </select>
                    </div>
                </div>
                <div class="col-1"></div>
                <div v-if="coursesPlateMsg" class="col-9 shadow rounded ml-5 p-3 second-float">
                    {{ coursesPlateMsg }}
                </div>
                <div v-else-if="!pending" class="col-9 shadow rounded ml-5 p-3 second-float">
                    <ListCoursesCarusel :data="courses" />
                </div>
                <div v-else class="col-9 shadow rounded ml-5 p-3 second-float loading-back">
                    <div class="spinner-border" id="loadingSpinner" role="status">
                        <span class="visually-hidden">Загрузка...</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
.loading-back {
    height: 20vh;

    display: flex;
    justify-content: center;
}

.spinner-border {
    margin-top: 7%;
    color: #53774B;
}
</style>
