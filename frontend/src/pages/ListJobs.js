import '../App.css';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import mammoth from "mammoth/mammoth.browser";
import {useNavigate} from "react-router-dom"; 


function ListJobs() {

    const navigate = useNavigate(); 

    
    function navigateTo() {
        navigate('/');
    
    }
    return (
        <div className="App">

        <h1>List Jobs Page</h1>
        
        <Stack spacing={60} direction="row">
            
            <Button variant="contained">Button</Button>        

            <Button variant="contained" onClick={navigateTo}> Go Back </Button>
        </Stack>
        </div>
  );
}

export default ListJobs;