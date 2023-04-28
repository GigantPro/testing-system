export const fetcher = (url, init) => fetch(url, init).then((res) => res.json());
