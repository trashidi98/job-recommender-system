import React from 'react'
import './OutlineContainer.css'
import OutlinedCard from './OutlinedCard';

function OutlineContainer({ jobsList }) {
  return (
    <div className='OutlineContainer'>
      {
        jobsList.map((job) => {
          return <OutlinedCard jobTitle={job.jobtitle} company={job.company} score={job.similarityscore} />
        })
      }
    </div>
  )
}

export default OutlineContainer;