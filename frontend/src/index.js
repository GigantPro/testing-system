import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { Auth } from './Padges/Auth';
import { Main } from './Padges/Main';
import { Header } from './Components/Header';
import { Footer } from './Components/Footer';

const root = ReactDOM.createRoot(document.getElementById('root'));

export default function App() {
    return (
        <div className='App'>
            <Header />
            <BrowserRouter>
                <Routes>
                    <Route path='/'>
                        <Route index element={<Main />} />
                        <Route path='auth' element={<Auth />} />
                    </Route>
                </Routes>
            </BrowserRouter>
            <Footer />
        </div>
    );
}

root.render(<App />);

reportWebVitals()
