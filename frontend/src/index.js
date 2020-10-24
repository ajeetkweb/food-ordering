import React from 'react';
import ReactDOM from 'react-dom'

import AppRouter from './router/index';


function App() {
    return (
        <div>
            <AppRouter/>
        </div>
    )
}

ReactDOM.render(
    <App />,
    document.getElementById("root")
)