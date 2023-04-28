import useSWR from 'swr';
import { fetcher } from '../Helpers/Fetcher';

export const useFetchMe = () => {
    return useSWR('/api/user/self/who_am_i', fetcher('/api/user/self/who_am_i'));
};
