import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import ListModels from './components/ListModels';
import * as serviceWorker from './serviceWorker';
import 'semantic-ui-css/semantic.min.css'
import { BrowserRouter, Switch, Route } from 'react-router-dom'

ReactDOM.render(
    <BrowserRouter>
        <Route path="/" exact={true} component={ListModels} />
        <Route path="/model" component={App} />
    </ BrowserRouter>
    , document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
