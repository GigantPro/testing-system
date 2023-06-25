<script setup>
const { data: top_of_courses, pending, error } = await useFetch('/api/course/most_popular')
</script>

<template>
    <div>
        <div v-if="top_of_courses" class="card-group text-center align-items-center justify-content-cente">
            <li v-for="item of top_of_courses" :key="item">
                <CourseCard :img_url="item.img_url" titel="item.titel" description="item.description" id="item.id" />
            </li>
        </div>
        <div v-else-if="{pending}" class="card-group text-center align-items-center justify-content-cente">
            <li v-for="index in 10" :key="index">
                <CourseCard />
            </li>
            {{ console.log(error, pending, top_of_courses) }}
            456
        </div>
        <div v-else class="card-group text-center align-items-center justify-content-cente">
            <h5 class="display-7 text-danger">Ошибка загрузки {{ error }}</h5>
        </div>
    </div>
</template>
