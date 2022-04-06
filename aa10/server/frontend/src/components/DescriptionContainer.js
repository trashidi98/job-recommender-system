import '../App.css';
import React, { useState } from 'react';
import './DescriptionContainer.css'
import {useNavigate, useLocation} from "react-router-dom"; 


function DescriptionContainer() {

    var location = useLocation(); 

    let description = location.state[2]; 
    let jobtitle = location.state[0]; 
    let company = location.state[1]; 

    return(
        <div>
            <div className="description-header">
            <h1> {`${jobtitle} @ ${company}`} </h1>
            </div>
            <div className="description-body">
                <h6>{description}</h6>
            </div>
        </div>
    );
}

export default DescriptionContainer; 