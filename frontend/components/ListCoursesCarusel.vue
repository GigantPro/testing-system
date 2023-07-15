<script setup>
const props = defineProps(['data'])
</script>

<template>
    <div class="container-fluid row p-2 m-2">
        <div v-for="item in props.data" :key="item" class="col-xxl-3 col-xl-3 col-lg-3 col-md-6 col-sm-12">
            <CourseCard :item_="item" />
        </div>
        <div class="card more-courses-card text-center justifycontent-center col-xxl-3 col-xl-3 col-lg-3 col-md-6 col-sm-12">
            <div class="row"></div>
            <div class="row card-body text-center align-items-center justify-content-center">
                <NuxtLink to="/courses/list" class="btn btn-info text-white btn-secondary">Больше
                    курсов</NuxtLink>
            </div>
            <div class="row"></div>
        </div>
    </div>
</template>

<style scoped>
.more-courses-card {
    background-color: #53774B;
}
</style>
