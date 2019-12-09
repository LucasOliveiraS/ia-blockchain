import React from 'react'
import { Header, Icon } from 'semantic-ui-react'

export const HeaderIMDB = () => (
  <Header as='h2'>
    <Icon name='cubes' />
    <Header.Content>
      IA-Blockchain
      <Header.Subheader>IMDB Movies</Header.Subheader>
    </Header.Content>
  </Header>
)