import React, {useLayoutEffect, useEffect, useState} from 'react';
import './App.css';
import { HeaderIMDB } from './components/Header'
import { ListModels } from './components/ListModels'
import TabExampleSecondaryPointing, { Tab } from './components/Tab'
import { StatisticExampleGroup } from './components/StatisticData'
import { Container } from 'semantic-ui-react';
import web3 from './web3';

function App() {

  async function fetchMyAPI() {

    const accounts = await window.ethereum.enable();
    const account = accounts[0];

    console.log(account)

    const response = await fetch('/address', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(account)
  })

    if(response.ok) {
      console.log("Response worked!")
    } else{
      console.log("Not worked!")
    }
  }

  setTimeout(function(){  }, 3000);
  useEffect(() => {
    fetchMyAPI();
  }, []);

  return (
    <Container style={{ marginTop: 40 }}>
      <HeaderIMDB></HeaderIMDB>
      <TabExampleSecondaryPointing />
      <div style={{ marginTop: 40 }}></div>
      <StatisticExampleGroup />
    </Container>
    
  );
}

export default App;