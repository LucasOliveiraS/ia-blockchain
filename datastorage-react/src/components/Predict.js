import React, { useState, useLayoutEffect, Component } from 'react';
import { Form, Input, FormField, Button, Segment} from 'semantic-ui-react';

export const PredictForm = () => {
    const [input, setInput] = useState('')
    const [output, setOutput] = useState('')
    
    useLayoutEffect(() => {
        fetch("/predict").then(response =>
        response.json().then(output => {
            console.log(output)
        })
        );
    }, []);

    return(
        <Form>
            <Form.Field>
                <p>Input:</p>
                <Input placeholder="" value={input} onChange={e => setInput(e.target.value)} />
                <Segment>{output}</Segment>
            </Form.Field>
        
            <Form.Field>
                <Button onClick={async () => {
                    const inputData = { input }
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(inputData)
                    })

                    if(response.ok) {
                        console.log("Response worked!")
                    } else{
                        console.log("Not worked!")
                        console.log(inputData['input'])
                    }

                    const data = await response.json();
                    setOutput(data.output);
                    console.log('Saída: ',data.output);
                }}>
                    submit
                </Button>

            </Form.Field>

        </Form>
    );
}