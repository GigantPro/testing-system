import { useFetchMe, useLogin } from '../Api/Auth';

import { useState } from 'react';

import closePassword from './assets/close_password.png';
import openPassword from './assets/open_password.png';

import './styles/Auth.scss';

export const Auth = () => {
    const { loginIncorrect, setLoginIncorrect } = useState(false);
    const { startLogin, setStartLogin } = useState(false);

    function showPassword() {
        let passwordInput = document.getElementsByClassName('auth-password-input')[0];
        let passwordStatusImg = document.getElementsByClassName('password-status-img')[0];
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

    const Login = () => {
        let passwordInput = document.getElementsByClassName('auth-password-input')[0];
        let loginInput = document.getElementsByClassName('auth-login-input')[0];
        console.log(passwordInput.value, loginInput.value);

        const password = passwordInput.value;
        const login = loginInput.value;

        // const [data, error] = useLogin(login, password);
        console.log(data, error);
    };

    if (startLogin) {
        const [data, error] = useLogin(login, password);
    }

    const { data, isLoading } = useFetchMe();

    if (data && data.detail === 'Unauthorized') {
        return (
            <div className='auth_wigit'>
                <div className='login_form'>
                    <b className='login_msg'>Войти</b>
                    <p />
                    <input type='text' className='auth-login-input' placeholder='Логин' />
                    <div className='password-pole'>
                        <input
                            type='password'
                            className='auth-password-input'
                            placeholder='Пароль'
                        />
                        <button className='show-password-button' onClick={showPassword}>
                            <img
                                src={openPassword}
                                alt='Open password'
                                className='password-status-img'
                            />
                        </button>
                    </div>
                    <button className='accept-button' onClick={Login}>
                        √
                    </button>
                </div>
            </div>
        );
    } else if (loginIncorrect) {
        return (
            <div className='auth_wigit'>
                <div className='login_form'>
                    <b className='login_msg'>Войти</b>
                    <p />
                    <input type='text' className='auth-login-input' placeholder='Логин' />
                    <div className='password-pole'>
                        <input
                            type='password'
                            className='auth-password-input'
                            placeholder='Пароль'
                        />
                        <button className='show-password-button' onClick={showPassword}>
                            <img
                                src={openPassword}
                                alt='Open password'
                                className='password-status-img'
                            />
                        </button>
                        <p className='incorrect-data'>Неправильные логин или пароль!</p>
                    </div>
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
