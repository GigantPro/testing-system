export const fetcher = (url, init, ...args) => fetch(url, init, ...args).then((res) => res.json());
