<script>
export default {
    name: 'CourseCard',
    props: [
        'img_url',
        'titel',
        'description',
        'id',
    ],
}
</script>

<template>
    <div>
    <div v-if="titel" class="card">
        <img :src="img_url" class="card-img-top" alt="Картинка">

        <div class="card-body">
            <h5 class="card-title">{{ titel }}</h5>
            <p class="card-text">{{ description }}</p>
            <a href="#" class="btn btn-primary">Перейти к курсу</a>
        </div>
    </div>
    <div v-else class="card">
        <img src="https://media.tenor.com/7t8foti8FG8AAAAC/loading-screen-cat.gif" class="card-img-top" alt="Картинка">
        <div class="card-body">
            <h5 class="card-title placeholder-glow">
                <span class="placeholder col-6"></span>
            </h5>
            <p class="card-text placeholder-glow">
                <span class="placeholder col-7"></span>
                <span class="placeholder col-4"></span>
                <span class="placeholder col-4"></span>
                <span class="placeholder col-6"></span>
                <span class="placeholder col-8"></span>
            </p>
            <a class="btn btn-primary disabled placeholder col-6"></a>
        </div>
    </div>
    </div>
</template>