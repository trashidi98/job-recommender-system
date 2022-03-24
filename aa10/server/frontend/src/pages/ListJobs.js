import '../App.css';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import OutlinedCard from '../components/OutlinedCard';

import OutlineContainer from '../components/OutlineContainer'

const jobsFullList = {
    "jobs": [
        {
            "jobtitle": "JOB_TITLE1",
            "company": "COMPANY1",
            "similarityscore": "93%"
        },
        {
            "jobtitle": "JOB_TITLE2",
            "company": "COMPANY2",
            "similarityscore": "93%"
        },
        {
            "jobtitle": "JOB_TITLE3",
            "company": "COMPANY3",
            "similarityscore": "89%"
        },
        {
            "jobtitle": "JOB_TITLE4",
            "company": "COMPANY4",
            "similarityscore": "87%"
        },
        {
            "jobtitle": "JOB_TITLE5",
            "company": "COMPANY5",
            "similarityscore": "86%"
        },
        {
            "jobtitle": "JOB_TITLE6",
            "company": "COMPANY6",
            "similarityscore": "85%"
        },
        {
            "jobtitle": "JOB_TITLE7",
            "company": "COMPANY7",
            "similarityscore": "85%"
        },
        {
            "jobtitle": "JOB_TITLE8",
            "company": "COMPANY8",
            "similarityscore": "83%"
        },
        {
            "jobtitle": "JOB_TITLE9",
            "company": "COMPANY9",
            "similarityscore": "82%"
        },
        {
            "jobtitle": "JOB_TITLE10",
            "company": "COMPANY10",
            "similarityscore": "70%"
        }

    ]
}
const jobsList = jobsFullList.jobs
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
                <OutlineContainer jobsList={jobsList}></OutlineContainer>
            </div>
        </div>

    );
}

export default ListJobs;