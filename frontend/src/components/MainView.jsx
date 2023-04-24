import './styles/MainView.scss';
import notifyIco from './assets/notify.png';
import React from 'react';
import axios from 'axios';

class MainView extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: {},
        };
    }

    render() {
        return (
            <div className='MainView'>
                {this.getHeader()}
                <div className='main_content'></div>
            </div>
        );
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

    login() {}

    registrate() {}

    getHeader() {
        const { error, isLoaded, items } = this.state;
        if (error) {
            console.log(error.message);
            return (
                <div className='header'>
                    <div className='loginButtons'>
                        <button className='loginButton' onClick={this.login}>
                            Вход
                        </button>
                        <button className='registredButton' onClick={this.registrate}>
                            Регистрация
                        </button>
                    </div>
                </div>
            );
        } else if (!isLoaded) {
            return <div className='header'>Loading...</div>;
        } else {
            return (
                <div className='header'>
                    <div className='Accaunt'>
                        <button className='AccauntButton'>
                            <img src={items.ico_url} alt='ico' />
                            <div className='UserName'>{items.name}</div>
                        </button>
                        <button className='NotifyButton'>
                            <img src={notifyIco} alt='notifyIco' className='notyfiImg' />
                        </button>
                    </div>
                </div>
            );
        }
    }
}

export default MainView;
