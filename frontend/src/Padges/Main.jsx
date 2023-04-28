import { useFetchMe } from '../Api/Auth';

export const Main = () => {
    const { data, error } = useFetchMe();

    if (!data && !error) {
        return <div>Loading...</div>;
    } else if (data) {
        return <div className='header'>{data}</div>;
    } else if (error) {
        return (
            <div className='header'>
                <div className='loginButtons'>
                    <button
                        className='loginButton'
                        onClick={(event) => (window.location.href = '/auth')}
                    >
                        Вход
                    </button>
                    <button
                        className='registredButton'
                        onClick={(event) => (window.location.href = '/auth')}
                    >
                        Регистрация
                    </button>
                </div>
            </div>
        );
    }
};
