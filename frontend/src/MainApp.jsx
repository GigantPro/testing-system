import { Login } from './Padges/Login';
import { Registration } from './Padges/Registration';
import { Main } from './Padges/Main';
import { Header } from './Components/Header';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Footer } from './Components/Footer';
import './Main.scss';

export const MainApp = () => {
    return (
        <div className='App'>
            <Header />
            <BrowserRouter>
                <Routes>
                    <Route path='/'>
                        <Route index element={<Main />} />
                        <Route path='login' element={<Login />} />
                        <Route path='registration' element={<Registration />} />
                    </Route>
                </Routes>
            </BrowserRouter>
            <Footer />
        </div>
    );
};
