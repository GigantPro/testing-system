import { useFetchMe } from '../Api/Auth';
import notifyIco from './assets/notify.png';

import './styles/Header.scss';

export const Header = () => {
    const { data } = useFetchMe();

    if (!data) {
        return <div>Loading...</div>;
    } else if (data.detail === 'Unauthorized') {
        return (
            <div className='header'>
                <div className='loginButtons'>
                    <button
                        className='loginButton'
                        onClick={(event) => (window.location.href = '/login')}
                    >
                        Вход
                    </button>
                    <button
                        className='registredButton'
                        onClick={(event) => (window.location.href = '/registration')}
                    >
                        Регистрация
                    </button>
                </div>
            </div>
        );
    } else if (data) {
        return (
            <div className='header'>
                <div className='Accaunt'>
                    <button className='AccauntButton'>
                        <img src={data.ico_url} alt='ico' className='accauntIco' />
                        <div className='UserName'>{data.name}</div>
                    </button>
                    <button className='NotifyButton'>
                        <img src={notifyIco} alt='notifyIco' className='notyfiImg' />
                    </button>
                </div>
            </div>
        );
    }
};
