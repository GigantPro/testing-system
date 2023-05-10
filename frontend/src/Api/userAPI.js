import { $authHost, $host } from './index';

export const registration = async (email, password, username, name, surname, ico_url) => {
    try {
        const response = await $host.post(
            '/api/auth/register',
            { email, username, password, name, surname, ico_url, role_id: 1 },
            { headers: { 'Content-Type': 'application/json', Accept: 'application/json' } },
        );
        return response;
    } catch {
        return null;
    }
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
    return response;
};

export const uploadImg = async (filedata) => {
    try {
        const formData = new FormData();
        formData.append('filedata', filedata.replace('data:', '').replace(/^.+,/, ''));
        formData.append('file_type', filedata.split(';')[0].split('/')[1]);
        const response = await $host.post('/api/user/upload/avatar', formData, {
            headers: {
                Accept: 'application/json',
                'Content-Type': 'multipart/form-data',
            },
        });

        return response.data;
    } catch (e) {
        return null;
    }
};
