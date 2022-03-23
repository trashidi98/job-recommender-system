import '../App.css';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import {useNavigate} from "react-router-dom"; 
import OutlinedCard from '../components/OutlinedCard'; 


function ListJobs() {

    const navigate = useNavigate(); 
    
    function navigateTo() {
        navigate('/');
    }

    return (
        <div>
        
            <div className="list-jobs">
                <h1>Recommended Jobs</h1>
            </div>

            <div className="list-jobs">
                <OutlinedCard jobTitle={"Software Dev"} company={"SHAHBAZ"} score={"10"}></OutlinedCard>
            </div> 
        </div>

  );
}

export default ListJobs;