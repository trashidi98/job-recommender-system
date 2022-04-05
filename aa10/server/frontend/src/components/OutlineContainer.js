import React from 'react'
import './OutlineContainer.css'
import OutlinedCard from './OutlinedCard';

function changeName(company) {

  let rancompanies = ["Dropper", "Connecting Services", "Looper", "StackAssist", "Gamification", "Integrate Inc", "Tata Consultancy", "Honeymade Devices", "AdaFruit Inc", "Ansys Co."]

  if (company.length > 25) {
    return company = rancompanies[Math.floor(Math.random() * rancompanies.length)];
  }

  else {
    return company;
  }
}
function changeJobTitle(jobtitle) {

  let rancompanies = ["Software Developer", "Software Engineer", "Data Scientist", "Data Engineer", "Data Analyst", "Developer", "Engineer"]

  if (jobtitle.length > 25) {
    return jobtitle = rancompanies[Math.floor(Math.random() * rancompanies.length)];
  }

  else {
    return jobtitle;
  }
}
function OutlineContainer({ jobsList }) {
  return (
    <div className='OutlineContainer'>
      {
        jobsList.map((job) => {
          return <OutlinedCard jobTitle={changeJobTitle(job.jobtitle)} company={changeName(job.company)} score={job.similarity} />
        })
      }
    </div>
  )
}

export default OutlineContainer;
