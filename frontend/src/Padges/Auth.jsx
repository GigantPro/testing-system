import { useFetchMe } from '../Api/Auth';

import { useState } from 'react';

import closePassword from './assets/close_password.png';
import openPassword from './assets/open_password.png';

import './styles/Auth.scss';
import { login } from '../Api/userAPI';

export const Auth = () => {
    const [beforSubmtButText, setBeforSubmtButText] = useState('');
    const [loginText, setLoginText] = useState('');
    const [password, setPassword] = useState('');

    const { data, isLoading } = useFetchMe();

    function showPassword() {
        const passwordStatusImg = document.getElementsByClassName('password-status-img')[0];
        const passwordInput = document.getElementsByClassName('auth-password-input')[0];
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            passwordStatusImg.src = closePassword;
        } else if (passwordInput.type === 'text') {
            passwordInput.type = 'password';
            passwordStatusImg.src = openPassword;
        } else {
            console.log('Incorrect logic');
        }
    }

    const Login = async () => {
        const res = await login(loginText, password);

        if (!res) {
            setBeforSubmtButText('Неправильная почта или пароль');
        } else {
            window.location.href = '/';
        }
    };

    if (data && data.detail === 'Unauthorized') {
        return (
            <div className='auth_wigit'>
                <div className='login_form'>
                    <b className='login_msg'>Войти</b>
                    <p />
                    <input
                        type='text'
                        className='auth-login-input'
                        placeholder='Логин'
                        value={loginText}
                        onChange={(e) => setLoginText(e.target.value)}
                    />
                    <div className='password-pole'>
                        <input
                            type='password'
                            className='auth-password-input'
                            placeholder='Пароль'
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <button className='show-password-button' onClick={showPassword}>
                            <img
                                src={openPassword}
                                alt='Open password'
                                className='password-status-img'
                            />
                        </button>
                    </div>
                    <p className='incorrect-data'>{beforSubmtButText}</p>
                    <button className='accept-button' onClick={Login}>
                        √
                    </button>
                </div>
            </div>
        );
    } else if (!isLoading) {
        return 'Loading...';
    } else if (data) {
        return '34534534';
    }
};
