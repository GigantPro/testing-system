import './styles/Auth.scss';
import React from 'react';
import axios from 'axios';

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

    next() {}

    registrate() {}

    getAuth() {
        const { error, isLoaded, isLogged } = this.state;
        if (error) {
            return (
                <div className="auth_wigit">
                    <p className='login_msg'>Войти</p>
                    <input type="text" value='Логин' />
                </div>
            );
        } else if (!isLoaded) {
            return 'Loading...';
        } else if (isLogged){
            return '34534534';
        }
    }
}

export default Auth;
