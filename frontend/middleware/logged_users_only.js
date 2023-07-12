export default defineNuxtRouteMiddleware(async (to, from) => { // Fix me: Если есть return, то всегда приходит к нему
    const headers = useRequestHeaders()
    const { data: user_data, pending } = await useFetch(
        "http://backend:5001/user/self/who_am_i",
        { headers: headers, server: true }
    );
    console.log(user_data.value);
    const user = user_data.value;
    if (!user) {
        console.log('No');
        console.log(pending);
        return '/'
    } else {
        console.log('yes');
        console.log(pending);
    }
  })