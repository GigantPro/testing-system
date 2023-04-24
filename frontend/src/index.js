import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './index.css';
import Auth from './components/Auth';
import MainView from './components/MainView';
import SiteHeader from './components/SiteHeader';

const root = ReactDOM.createRoot(document.getElementById('root'));

export default function App() {
    return (
        <div className='App'>
            <SiteHeader />
            <BrowserRouter>
                <Routes>
                    <Route path='/'>
                        <Route index element={<MainView />} />
                        <Route path='auth' element={<Auth />} />
                    </Route>
                </Routes>
            </BrowserRouter>
        </div>
    );
}

root.render(<App />);
