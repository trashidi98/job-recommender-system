import '../App.css';
import React, { useState } from 'react';
import './DescriptionContainer.css'
import {useNavigate, useLocation} from "react-router-dom"; 
import logo from "./logo_jobhunter.png";



function DescriptionContainer() {

    var location = useLocation(); 

    let description = location.state[2]; 
    let jobtitle = location.state[0]; 
    let company = location.state[1]; 
    let label = location.state[3];

    return(
        <div>
            <div className="description-header">
            <h1> {`${jobtitle} @ ${company}`} </h1>
            </div>
            <div className="description-body">
                <h3>Description</h3>
                <h6>{description}</h6>
                <h3>Key Hidden Topics Found in the Job Posting</h3>
                <h6><br/>{label.map((label)=>label +"\n" + ","+"\n")}</h6>
            </div>

            <div>
              <img src={logo} width={250} height={150} alt="logo"/>
            </div> 
        </div>
    );
}

export default DescriptionContainer; 