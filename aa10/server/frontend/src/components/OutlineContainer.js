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

function changeJobTitle(jobtitle) {

  let rantitles = ["Software Developer", "Software Engineer", "Data Scientist", "Data Engineer", "Data Analyst", "Developer", "Engineer"]

  if (jobtitle.length > 25) {
    return jobtitle = rantitles[Math.floor(Math.random() * rantitles.length)];
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
              return <OutlinedCard jobTitle={changeJobTitle(job.jobtitle)} company={changeName(job.company)} score={job.similarity} description={job.description} label={job.Labels}/>
            })
        }
    </div>
  )
}

export default OutlineContainer;
