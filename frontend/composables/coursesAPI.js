export const useMostPopular = async (count = 10) => {
    let url = null;
    let props = null;
    if (process.client){
        url = '/api/course/most_popular?count='+count;
        props = { server: false };
    } else if (process.server) {
        url = 'http://backend:5001/course/most_popular?count='+count;;
        props = { server: true };
    }
    return await useFetch(url, props);
}