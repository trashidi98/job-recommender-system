import '../App.css';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import Lottie from 'react-lottie'; 
import AnimatedCube from '../lotties/cube-animation';  


function LoadingScreen() {

    const navigate = useNavigate();

    function navigateTo() {
        navigate('/ListJobs');
    }

    const defaultOptions = {
        loop: true,
        autoplay: true,
        animationData: AnimatedCube,
        rendererSettings: {
          preserveAspectRatio: "xMidYMid slice"
        }
      };

    return (
        <div className="App">
            <header className="App-header">
                <Lottie
                options={defaultOptions}
                height={600}
                width={600}/>
            </header>
        </div>

    );
}

export default LoadingScreen;