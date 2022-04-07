import '../App.css';
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
import './JobDescription.css'
import DescriptionContainer from '../components/DescriptionContainer';
import ArrowCircleLeftOutlinedIcon from '@mui/icons-material/ArrowCircleLeftOutlined';
import { IconButton } from '@mui/material';



function JobDescription() {

    var location = useLocation(); 
    const navigate = useNavigate(); 

    function navigateBack() {
      navigate('/ListJobs', {state: true});
    }

    return (
        <div className="job-description-main">

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

          {/* <div className="back-button">
            <IconButton color="secondary" size='large' onClick={navigateBack}>
              <ArrowCircleLeftOutlinedIcon sx={{fontSize: '65px'}}/>
            </IconButton>
          </div> */}
                        
            <div className="job-description-body">
                <DescriptionContainer/>
            </div>        
            
        </div>
    )
}

export default JobDescription; 