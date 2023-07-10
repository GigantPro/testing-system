<template>
    <div>
        <NavBar />
        <NuxtPage class="main_content" />
        <Footer />
    </div>
</template>


<script setup>
useHead({
    link: [
        {
            href: "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
            rel: "stylesheet",
            integrity: "sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM",
            crossorigin: "anonymous"
        }
    ],
    script: [
        {
            src: "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
            integrity: "sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz",
            crossorigin: "anonymous"
        }
    ],
    title: 'Xiver education',
    meta: [
        { name: 'description', content: 'Сайт для удобного обучения и преподавания' }
    ],
})
</script>

<style>
body {
    background: url("~/assets/background.svg") right top no-repeat;
}

.main_content {
    padding: .3rem;
    margin: auto .5rem auto .5rem;
}

.input-required::after {
    color: red;
    content: '*';
    margin-left: .2rem;
}
</style>
