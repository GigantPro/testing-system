import './styles/SiteHeader.scss';
import notifyIco from './assets/notify.png';
import React from 'react';
import axios from 'axios';

class SiteHeader extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: {},
        };
    }

    render() {
        return <div className='site_header'>{this.getHeader()}</div>;
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

    getHeader() {
        const { error, isLoaded, items } = this.state;
        if (error) {
            console.log(error.message);
            return (
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
            );
        } else if (!isLoaded) {
            return 'Loading...';
        } else {
            return (
                <div className='Accaunt'>
                    <button className='AccauntButton'>
                        <img src={items.ico_url} alt='ico' className='accauntIco' />
                        <div className='UserName'>{items.name}</div>
                    </button>
                    <button className='NotifyButton'>
                        <img src={notifyIco} alt='notifyIco' className='notyfiImg' />
                    </button>
                </div>
            );
        }
    }
}

export default SiteHeader;
