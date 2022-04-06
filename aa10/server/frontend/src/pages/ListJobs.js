import '../App.css';
import './ListJobs.css'
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import mammoth from "mammoth/mammoth.browser";
import {useNavigate, useLocation} from "react-router-dom"; 
import Axios from "axios";
import OutlinedCard from '../components/OutlinedCard';
import OutlineContainer from '../components/OutlineContainer';
import CountUp from 'react-countup';
import Particles from "react-tsparticles";


function zip(arrays) {
    return arrays[0].map(function(_,i){
        return arrays.map(function(array){return array[i]})
    });
}

function createJobObject(zippedArray) {

    let object = {}; 

    object["jobtitle"] = zippedArray[0];
    object["company"] = zippedArray[1];
    object["similarity"] = zippedArray[2]; 
    object["description"] = zippedArray[3];    

    return object; 
}

function processResults(backendObject) {

    var fullJobsArray = []; 

    let jobTitlesArr = backendObject["job_title"]; 

    let companyArr = backendObject["company_name"]; 

    let similarityArr = backendObject["Similarity"]; 

    let jobDescriptionArr = backendObject["job_description"];

  let zippedArrays = zip([jobTitlesArr, companyArr, similarityArr, jobDescriptionArr])

    for(let i = 0; i < jobTitlesArr.length; i++ ) {
        fullJobsArray.push(createJobObject(zippedArrays[i]));  
    } 

    return fullJobsArray; 

}


function ListJobs() {

    var location = useLocation(); 

    const navigate = useNavigate(); 

    let backendData = location.state; 

    let processedResults = processResults(backendData); 
    
    function navigateBack() {
        navigate('/');
    }

    return (
  
    <div className="list-jobs-main">

<Particles params={{
      fpsLimit: 30,
      particles: {
        color: {
          value: "#9400D3"
        },
        links: {
          enable: true,
          color: "#9c4be7",
          distance: 125
        },
        move: {
          enable: true
        }
      }
    }}/>      
  <div style={{
      position: "absolute",
  }}>

  <div className="list-jobs-main">
        
        <div className="list-jobs">
            <h1>Recommended Jobs</h1>
        </div>

        <div>
        <Button variant="contained" color="secondary" onClick={navigateBack}> Go Back </Button>
        </div>

        <div className="list-jobs">
            <OutlineContainer jobsList={processedResults}></OutlineContainer>
        </div>
        </div>
    </div>
  </div>

  );
}

export default ListJobs;