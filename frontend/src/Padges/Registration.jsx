import { useFetchMe } from '../Api/Auth';

import { useState, useRef } from 'react';

import './styles/Registration.scss';
import { registration as registrationAPI, uploadImg } from '../Api/userAPI';

export const Registration = () => {
    const { data, isLoading } = useFetchMe();

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');
    const [username, setUsername] = useState('');
    const [surname, setSurname] = useState('');
    const [name, setName] = useState('');
    const [customIco, setCustomIco] = useState('')

    const fileReader = new FileReader();
    fileReader.onloadend = () => {
        setCustomIco(fileReader);
    };

    const ico_url = '/api/static/standart_ico.png';

    const handleFile = (event) => {
        const userFile = event.target.files[0];
        fileReader.readAsDataURL(userFile);
    };

    const Registrate = async (event) => {
        event.preventDefault();
        
        let userIco = ico_url;

        if (customIco) {
            userIco = await uploadImg(customIco);
            console.log(customIco);
        }
        console.log(userIco);

        // const res = await registrationAPI(email, password, username, name, surname, ico_url);

        // if (!res) {
        //     console.log('Неправильная почта или пароль');
        // } else {
        //     window.location.href = '/';
        // }
    };

    if (data && data.detail === 'Unauthorized') {
        return (
            <div className='registration_wigit'>
                <b className='registrationLale'>Регистрация</b>
                <form onSubmit={Registrate} className='registration-form'>
                    <div className='inputs'>
                        <div className='left-column'>
                            <input
                                type='text'
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                placeholder='Имя'
                            />
                            <input
                                type='text'
                                value={surname}
                                onChange={(e) => setSurname(e.target.value)}
                                placeholder='Фамилия'
                            />
                            <input
                                type='text'
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                placeholder='Псевдоним'
                            />
                        </div>
                        <div className='right-column'>
                            <input
                                type='text'
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                placeholder='Почта'
                            />
                            <input
                                type='password'
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                placeholder='Пароль'
                            />
                            <input
                                type='password'
                                value={password2}
                                onChange={(e) => setPassword2(e.target.value)}
                                placeholder='Подтвердите пароль'
                            />
                        </div>
                        <div className='imagine-div'>
                            <img
                                className='user-avatar-img'
                                src={customIco ? customIco.result : ico_url}
                                alt='ico'
                            />
                            <input
                                className='change-Imagine'
                                accept='image/*'
                                type='file'
                                id='button-file'
                                onChange={handleFile}
                            />
                        </div>
                    </div>
                    <button type='submit' className='submit-button'>
                        Зарегистрироваться
                    </button>
                </form>
            </div>
        );
    } else if (!isLoading) {
        return 'Loading...';
    } else if (data) {
        return '34534534';
    }
};
