// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      apiBase: '/nuxt-api'
    }
  },
  css: [
    '~/assets/css/config.scss',
  ],
})
