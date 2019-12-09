import React, { useState, useLayoutEffect } from 'react'
import { Statistic, Icon } from 'semantic-ui-react'

export const StatisticExampleGroup = () => {

  const [data, setData] = useState('')
  const [accuracy, setAccuracy] = useState('')

  useLayoutEffect(() => {
    fetch("/get_data").then(response =>
      response.json().then(data => {
        setData(data.data);
      })
    ); 
  }, []);

  useLayoutEffect(() => {
    fetch("/get_accuracy").then(response =>
      response.json().then(accuracy => {
        setAccuracy(accuracy.accuracy);
      })
    ); 
  }, []);

  return(
  <div>
    <Statistic.Group>
      <Statistic>
        <Statistic.Value>
        {accuracy}
        </Statistic.Value>
        <Statistic.Label>Accuracy</Statistic.Label>
      </Statistic>
      <Statistic>
        <Statistic.Value>
        {data}
        </Statistic.Value>
        <Statistic.Label>Data Sample</Statistic.Label>
      </Statistic>
      <Statistic>
        <Statistic.Value>2</Statistic.Value>
        <Statistic.Label>Blockchain Members</Statistic.Label>
      </Statistic>
    </Statistic.Group>
  </div>
  );
}

