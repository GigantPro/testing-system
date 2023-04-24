import './styles/Auth.scss';
import React from 'react';
import axios from 'axios';

import closePassword from './assets/close_password.png';
import openPassword from './assets/open_password.png';

class Auth extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: {},
            isLogged: false,
        };
    }

    render() {
        return <div className='auth'>{this.getAuth()}</div>;
    }

    componentDidMount() {
        axios
            .get('/api/user/self/who_am_i')
            .then((res) => res.data)
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result,
                        isLogged: true,
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error,
                    });
                },
            );
    }

    showPassword() {
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

    login() {
        let passwordInput = document.getElementsByClassName('auth-password-input')[0];
        let loginInput = document.getElementsByClassName('auth-login-input')[0];
        console.log(loginInput.value, passwordInput.value, 123);
        const username = loginInput.value;
        const password = passwordInput.value;
        axios
            .post('/api/auth/login', data={ username: username, password: password })
            .then((res) => res.data)
            .then(
                (result) => {
                    this.setState({
                        isLoggedPasswordRequest: true,
                        items: result,
                    });
                    console.log(res.data);
                },
                (error) => {
                    this.setState({
                        isLoggedPasswordRequest: true,
                        error,
                    });
                    console.log(error.message);
                },
            );
    }

    getAuth() {
        const { error, isLoaded, isLogged } = this.state;
        if (error) {
            console.log(error.code);
            if (error.code === 'ERR_BAD_REQUEST') {
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
                                <button
                                    className='show-password-button'
                                    onClick={this.showPassword}
                                >
                                    <img
                                        src={openPassword}
                                        alt='Open password'
                                        className='password-status-img'
                                    />
                                </button>
                            </div>
                            <button className='accept-button' onClick={this.login}>
                                √
                            </button>
                        </div>
                    </div>
                );
            } else if (error.code === 400) {
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
                                <button
                                    className='show-password-button'
                                    onClick={this.showPassword}
                                >
                                    <img
                                        src={openPassword}
                                        alt='Open password'
                                        className='password-status-img'
                                    />
                                </button>
                                <p className='incorrect-data'>Неправильные логин или пароль!</p>
                            </div>
                            <button className='accept-button' onClick={this.login}>
                                √
                            </button>
                        </div>
                    </div>
                );
            }
        } else if (!isLoaded) {
            return 'Loading...';
        } else if (isLogged) {
            return '34534534';
        }
    }
}

export default Auth;
