import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { MainApp } from './MainApp';

const root = ReactDOM.createRoot(document.getElementById('root'));

export default function App() {
    return <MainApp />;
}

root.render(<App />);

reportWebVitals();
