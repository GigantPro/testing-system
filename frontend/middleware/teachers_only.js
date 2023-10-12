export default defineNuxtRouteMiddleware(async (to) => {

    const { data: course_data } = await useAsyncData(
        'course_data_' + to.params.id,
        () => {
            const headers = useRequestHeaders()
    
            let api_url = ''
            if (process.server) api_url = process.env.SSR_API_BASE_URL + "/course/get/"
            else api_url = "/api/course/get/"
    
            api_url = api_url + to.params.id
    
            return $fetch( 
                api_url,
                { headers: headers},
            )
        },
    );
    const { data: user_data } = await useAsyncData(
        'who_am_i',
        () => {
            const headers = useRequestHeaders()
    
            let api_url = ''
            if (process.server) {api_url = process.env.SSR_API_BASE_URL + "/user/self/who_am_i"}
            else {api_url = "/api/user/self/who_am_i"}
            return $fetch(
                api_url,
                { headers: headers },
            )
        },
    );
    if (course_data.value.teachers_ids.indexOf(user_data.value.id) == -1) {
        throw createError({ statusCode: 403, statusMessage: 'Вы не учитель!' })
    }
})
