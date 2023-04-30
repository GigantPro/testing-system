import { $authHost, $host } from './index';

export const registration = async (email, password, username, name, surname, ico_url) => {
    const response = await $host.post(
        '/api/auth/login',
        { email, username, password, name, surname, ico_url },
        { headers: { 'Content-Type': 'application/json', Accept: 'application/json' } },
    );
    // localStorage.setItem('token', data.token);
    return response;
};

export const login = async (username, password) => {
    try {
        const response = await $host.post(
            '/api/auth/login',
            { username, password },
            { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } },
        );
        return response;
    } catch {
        return false;
    }
};

export const check = async () => {
    const response = await $authHost.get('user/auth');
    // localStorage.setItem('token', data.token);
    return response;
};
