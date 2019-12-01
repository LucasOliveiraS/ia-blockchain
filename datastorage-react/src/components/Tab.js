import React from 'react'
import { Tab } from 'semantic-ui-react'
import { TrainingForm } from './TrainingForm'
import { PredictForm } from './Predict'

const panes = [
  {
    menuItem: 'Predição',
    render: () => <Tab.Pane attached={false}><PredictForm /></Tab.Pane>,
  },
  {
    menuItem: 'Treino',
    render: () => <Tab.Pane attached={false}><TrainingForm /></Tab.Pane>,
  }
]

const TabExampleSecondaryPointing = () => (
  <Tab menu={{ secondary: true, pointing: true }} panes={panes} />
)

export default TabExampleSecondaryPointing