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
import ArrowCircleLeftOutlinedIcon from '@mui/icons-material/ArrowCircleLeftOutlined';
import { IconButton } from '@mui/material';
import logo from "./logo_jobhunter.png";

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
    object["Labels"] = zippedArray[4];

    return object; 
}

function processResults(backendObject) {

    var fullJobsArray = []; 

    let jobTitlesArr = backendObject["job_title"]; 

    let companyArr = backendObject["company_name"]; 

    let similarityArr = backendObject["Similarity"]; 

    let jobDescriptionArr = backendObject["job_description"];

    let labelsArr = backendObject["Labels"]; 

  let zippedArrays = zip([jobTitlesArr, companyArr, similarityArr, jobDescriptionArr, labelsArr])

    for(let i = 0; i < jobTitlesArr.length; i++ ) {
        fullJobsArray.push(createJobObject(zippedArrays[i]));  
        // console.log(labelsArr[0])
        // console.log(zippedArrays)

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

      <div className="back-button">
        <IconButton color="secondary" size='large' onClick={navigateBack}>
          <ArrowCircleLeftOutlinedIcon sx={{fontSize: '65px'}}/>
        </IconButton>
      </div>
    
        <div className="list-jobs">
            <h1>Recommended Jobs</h1>
        </div>

        <div className="list-jobs">
            <OutlineContainer jobsList={processedResults}></OutlineContainer>
        </div>

        <div>
          <img src={logo} width={250} height={150} alt="logo"/>
        </div>

        </div>
    </div>
  </div>

  );
}

export default ListJobs;