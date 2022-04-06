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



function JobDescription() {

    var location = useLocation(); 

    const navigate = useNavigate(); 

    function navigateTo() {
        navigate('/');
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
                        
            <div className="job-description-body">
                <DescriptionContainer/>
            </div>        
            
        </div>
    )
}

export default JobDescription; 