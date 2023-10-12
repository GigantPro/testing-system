export default defineNuxtRouteMiddleware(async () => {
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
    if (!user_data.value) {
        return '/auth?auth=login';
    }
})