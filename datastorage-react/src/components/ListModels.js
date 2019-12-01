import React, { useState } from 'react'
import { Dropdown } from 'semantic-ui-react'

const modelsOptions = [
    {
        key: 'IMDB Movies',
        text: 'IMDB Movies 96%',
        value: 'IMDB Movies'
    },
    {
        key: 'Digit Recognizer',
        text: 'Digit Recognizer 97%',
        value: 'Digit Recognizer'
    }
]

export const ListModels = () => {

    return (
        <Dropdown
        placeholder='Modelos disponíveis'
        fluid
        selection
        options={modelsOptions}
        />
    );
}
  