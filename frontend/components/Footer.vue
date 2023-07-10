<template>
<footer class="text-center text-lg-start rounded-top bg-dark text-white shadow">
  <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
  </section>

  <section class="">
    <div class="container text-center text-md-start mt-5">
      <!-- Grid row -->
      <div class="row mt-3">
        <!-- Grid column -->
        <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
          <!-- Content -->
          <h6 class="text-uppercase fw-bold mb-4">
            <i class="fas fa-gem me-3 text-secondary"></i>Xiver group
          </h6>
          <p>
            Мы команда разработчиков, которые делают то, что им нравится больше все - программируют. 
            <b>"Пока мы живы - код течет по нашим венам" (Александр Светлов)</b>
          </p>
        </div>
        <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
          <h6 class="text-uppercase fw-bold mb-4">
            Наши разработки
          </h6>
          <p>
            <NuxtLink to="https://xiver.ru" class="text-reset">Наш сайт</NuxtLink>
          </p>
          <p>
            <NuxtLink to="https://discord.com/api/oauth2/authorize?client_id=889092706935128074&permissions=8&scope=bot" class="text-reset">Discord бот</NuxtLink>
          </p>
          <p>
            <NuxtLink to="https://t.me/@xiver4_bot" class="text-reset">Telegram бот</NuxtLink>
          </p>
          <p>
            <NuxtLink to="/" class="text-reset">Xiver.Education</NuxtLink>
          </p>
        </div>

        <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
          <h6 class="text-uppercase fw-bold mb-4">
            Полезные ссылки
          </h6>
          <p>
            <NuxtLink to="https://discord.gg/7ECBEjjUw6" class="text-reset">Наш Discord</NuxtLink>
          </p>
        </div>

        <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
          <h6 class="text-uppercase fw-bold mb-4">Наши контакты</h6>
          <!-- <p><i class="fas fa-home me-3 text-secondary"></i> New York, NY 10012, US</p> -->
          <p>
            <i class="fas fa-envelope me-3 text-secondary"></i>
            gigantpro2000@gmail.com
          </p>
          <NuxtLink to="https://t.me/@gigantpro2000" class="text-reset">
            <i class="fas fa-envelope me-3 text-secondary"></i>
            Александр Светлов
          </NuxtLink>
          
          <!-- <p><i class="fas fa-phone me-3 text-secondary"></i> + 01 234 567 88</p>
          <p><i class="fas fa-print me-3 text-secondary"></i> + 01 234 567 89</p> -->
        </div>
      </div>
    </div>
  </section>

  <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.025);">
    © 2023 Copyright:
    <NuxtLink class="text-reset fw-bold" to="https://xiver.ru/">Xiver group</NuxtLink>
  </div>
</footer>
</template>

<style scoped>
footer {
    margin: 1rem .6rem 0rem .6rem;
}
</style>
