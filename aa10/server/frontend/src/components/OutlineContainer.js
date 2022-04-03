import React from 'react'
import './OutlineContainer.css'
import OutlinedCard from './OutlinedCard';
  
function changeName(company) {

  let rancompanies = ["Dropper", "Connecting Services", "Looper", "StackAssist", "Gamification", "Integrate Inc", "Tata Consultancy", "Honeymade Devices", "AdaFruit Inc", "Ansys Co."]

  if(company.length > 25) {
    return company = rancompanies[Math.floor(Math.random() * rancompanies.length)];
  }
  
  else{
    return company; 
  }
}

function OutlineContainer({ jobsList }) {
  return (
    <div className='OutlineContainer'>
        {
            jobsList.map((job) => {
            return <OutlinedCard jobTitle={job.jobtitle} company={changeName(job.company)} score={job.similarity} />
            })
        }
    </div>
  )
}

export default OutlineContainer;
