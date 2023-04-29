import useSWR from 'swr';
import { fetcher } from '../Helpers/Fetcher';

export const useFetchMe = () => {
    return useSWR('/api/user/self/who_am_i', fetcher);
};

export const useLogin = (username, password) => {
    return useSWR(
        '/api/auth/login',
        fetcher('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: JSON.stringify({
                username: username,
                password: password,
            }),
        }),
    );
};
