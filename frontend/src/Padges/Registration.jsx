import { useFetchMe } from '../Api/Auth';

import { useState, useRef } from 'react';

import './styles/Registration.scss';
import { registration as registrationAPI, uploadImg } from '../Api/userAPI';

import Avatar from 'react-avatar-edit';

export const Registration = () => {
    const { data, isLoading } = useFetchMe();

    const [statusFroUser, setStatusFroUser] = useState('');

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');
    const [username, setUsername] = useState('');
    const [surname, setSurname] = useState('');
    const [name, setName] = useState('');
    const [customIco, setCustomIco] = useState(null);

    const [cropedIco, setCropedIco] = useState(null);
    const [croopieModalActive, setCroopieModalActive] = useState(false);

    const icoRef = useRef(null);
    const customIcoRef = useRef(null);

    const fileReader = new FileReader();
    fileReader.onloadend = () => {
        setCustomIco(fileReader);
    };

    const ico_url = '/api/static/standart_ico.png';

    const CroopieModal = () => {
        let croppedImg = null;

        const onSave = () => {
            setCropedIco(croppedImg);
            setCroopieModalActive(false);
        };

        const onDiscard = () => {
            setCroopieModalActive(false);
        };

        // Fix me: когда снимаешь клик на областе с cropie_modal то он тоже деактивируется
        // Fix me: очень высокий выбор размеров аватарки
        return (
            <div
                className={croopieModalActive ? 'cropie_modal active' : 'cropie_modal'}
                onClick={() => setCroopieModalActive(false)}
            >
                <div className='cropie_modal_content' onClick={(e) => e.stopPropagation()}>
                    <Avatar
                        ref={customIcoRef}
                        src={customIco ? URL.createObjectURL(customIco) : null}
                        onCrop={(e) => (croppedImg = e)}
                        onClose={() => (croppedImg = null)}
                        imageWidth={1024}
                        width={1024}
                    />
                    <div className='modal_croop_buttons'>
                        <button className='modal_croop_button_save' onClick={onSave}>
                            Сохранить
                        </button>
                        <button className='modal_croop_button_discard' onClick={onDiscard}>
                            Отмена
                        </button>
                    </div>
                </div>
            </div>
        );
    };

    const handleChangeIco = (event) => {
        setCustomIco(event.target.files[0]);
        setCroopieModalActive(true);
    };

    const registrate = async (event) => {
        event.preventDefault();

        let userIco = ico_url;

        if (cropedIco) {
            console.log(cropedIco);
            userIco = await uploadImg(cropedIco);
        }
        console.log(userIco);

        const res = await registrationAPI(email, password, username, name, surname, userIco);

        console.log(res);
        if (!res) {
            setStatusFroUser('Что-то пошло не так');
        } else {
            window.location.href = '/';
        }
    };

    if (data && data.detail === 'Unauthorized') {
        return (
            <div className='registration_wigit'>
                <b className='registrationLale'>Регистрация</b>
                <CroopieModal />
                <form onSubmit={registrate} className='registration-form'>
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
                                type='email'
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
                                src={cropedIco ? cropedIco : ico_url}
                                alt='ico'
                            />
                            <button
                                className='change-ico-button'
                                onClick={() => icoRef.current.click()}
                                type='button'
                            >
                                Поменять аватарку
                            </button>
                            <input
                                hidden
                                pt='image/png, image/jpeg'
                                type='file'
                                id='button-file'
                                onChange={handleChangeIco}
                                ref={icoRef}
                            />
                        </div>
                    </div>
                    {statusFroUser}
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
