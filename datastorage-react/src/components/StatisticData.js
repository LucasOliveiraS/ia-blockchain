import React, { useState, useLayoutEffect } from 'react'
import { Statistic } from 'semantic-ui-react'

export const StatisticExampleGroup = () => {

  const [data, setData] = useState('')

  useLayoutEffect(() => {
    fetch("/get_data").then(response =>
      response.json().then(data => {
        setData(data.data);
      })
    ); 
  }, []);

  return(
  <div>
    <Statistic.Group>
      <Statistic>
        <Statistic.Value>{data}</Statistic.Value>
        <Statistic.Label>Data Sample</Statistic.Label>
      </Statistic>
      <Statistic>
        <Statistic.Value>3</Statistic.Value>
        <Statistic.Label>Blockchain Members</Statistic.Label>
      </Statistic>
    </Statistic.Group>
  </div>
  );
}

