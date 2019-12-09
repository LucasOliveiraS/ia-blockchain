import React, { useState } from 'react';
import { Form, Input, FormField, Button, Dropdown, Modal, Image, Header} from 'semantic-ui-react';

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
    const [reward, setReward] = useState(false)
    const [penalized, setPenalized] = useState(false)

    const getChange  =  (event, {value}) => {
        let choiceTarget = value;
        setTarget(choiceTarget);
    }

    const handleCloseReward = () => setReward(false)

    const handleClosePenalized = () => setPenalized(false)

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
            
                        const data = await response.json();
                        console.log('Saída: ',data.message);

                        if(data.message == 'True') {
                            setReward(true);
                        } else if(data.message == 'False') {
                            setPenalized(true);
                        }
                        
                    } else{
                        console.log("Not worked!")
                    }

                }}>
                    submit
                </Button>

            <Modal open={reward}
                onClose={handleCloseReward} basic size='small'>
                <Header icon='check' content='Você contribuiu com o modelo!' />
                <Modal.Content>
                <p>
                        Os dados foram analisados. Você melhorou nosso desempenho!
                </p>
                <p>
                    Recompensa: 0.31 Ether
                </p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick = {handleCloseReward}>Fechar</Button>
                </Modal.Actions>
            </Modal>

            <Modal open={penalized}
                onClose={handleClosePenalized} basic size='small'>
                <Header icon='x' content='Desculpe' />
                <Modal.Content>
                <p>
                    Os dados foram analisados. Você não melhorou nosso desempenho :(
                </p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick = {handleClosePenalized}>Fechar</Button>
                </Modal.Actions>
            </Modal>


            </Form.Field>
        </Form>
    );
}