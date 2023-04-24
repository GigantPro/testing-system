import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import MainView from './components/MainView';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <MainView />
    </React.StrictMode>,
);

reportWebVitals();
