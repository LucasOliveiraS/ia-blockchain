import React, {  Component , useState } from 'react'
import {Redirect, withRouter} from 'react-router-dom';
import { Dropdown, Container } from 'semantic-ui-react'

const modelsOptions = [
    {
        key: 'IMDB Movies',
        text: 'IMDB Movies 88%',
        value: 'IMDB Movies'
    },
    {
        key: 'House Prices',
        text: 'House Prices 91%',
        value: 'House Prices'
    }
]

export const ListModels = () => {

    const [target, setTarget] = useState('')

    const getChange  =  (event, {value}) => {
       
        window.location.href = "http://localhost:3000/model";
    }

    return (
        <Container>
        <div class="ui one column stackable center aligned page grid">
            <div class="column twelve wide">
                <h3 class="ui header">Selecione o modelo</h3>
                <Dropdown
                placeholder='Modelos disponíveis'
                fluid
                selection
                options={modelsOptions}
                onChange={getChange} 
                />
            </div>
        </div>
        </Container>
    );
}

export default ListModels;
  