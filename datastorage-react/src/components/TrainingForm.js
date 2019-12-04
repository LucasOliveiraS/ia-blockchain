import React, { useState } from 'react';
import { Form, Input, FormField, Button, Dropdown} from 'semantic-ui-react';

const labelOptions = [
    {
        key: 'Good',
        text: 'Good',
        value: '1'
    },
    {
        key: 'Bad',
        text: 'Bad',
        value: '-1'
    }
];

export const TrainingForm = () => {
    const [train, setTrain] = useState('')
    const [target, setTarget] = useState('')

    const getChange  =  (event, {value}) => {
        let choiceTarget = value;
        setTarget(choiceTarget);
    }

    return(
        <Form>
            <Form.Field>
                <p>Data Sample:</p>
                <Input placeholder="Training data" value={train} onChange={e => setTrain(e.target.value)} />
            </Form.Field>

            <Form.Field>
                <p>Target:</p>
                <Dropdown placeholder='target' fluid selection options={labelOptions} onChange={getChange} />
            </Form.Field>
        
            <Form.Field>
                <Button onClick={async () => {
                    const trainData = {'train' : train, 'label' : target}

                    const response = await fetch('/add_data', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(trainData)
                    })

                    if(response.ok) {
                        console.log("Response worked!")
                        window.ethereum.send('eth_sendTransaction', [{
                            "from": "0x690809206b73994282910F1740a729a89aF4beCa",
                            "to": "0xc0A08eB59ab5Fe19403d68555F4B51FC79c1B7b0",
                            "gas": "0x76c0", // 30400
                            "gasPrice": "0x9184e72a000", // 10000000000000
                            "value": "0x9184e72a"
                          }])
                        .then(function (result) {
                        // The result varies by method, per the JSON RPC API.
                        // For example, this method will return a transaction hash on success.
                        })
                        .catch(function (error) {
                        // Like a typical promise, returns an error on rejection.
                        })

                        const data = await response.json();
                        console.log('Saída: ',data.message);
                    } else{
                        console.log("Not worked!")
                    }

                }}>
                    submit
                </Button>
            </Form.Field>
        </Form>
    );
}