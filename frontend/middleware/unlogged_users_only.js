export default defineNuxtRouteMiddleware(async () => {
    const headers = useRequestHeaders()
    const { data: user_data } = await useFetch(
        "http://backend:5001/user/self/who_am_i",
        { headers: headers, server: true }
    );
    const user = user_data.value;
    if (user) {
        return '/';
    }
})