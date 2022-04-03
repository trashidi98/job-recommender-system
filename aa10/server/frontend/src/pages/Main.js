import React from 'react';
import {Routes, Route} from 'react-router-dom';
import '../App.css';
import ParticleComponent from './ParticlesContainer'
import HomePage from './HomePage';
import ListJobs from './ListJobs';
import LoadingScreen from'./LoadingScreen'; 
import Particles from "react-tsparticles";


const Main = () => {
  return (
  <Routes> {/* The Routes decides which component to show based on the current URL.*/}
    <Route exact path='/' element={<HomePage/>}></Route>
    <Route exact path='/Loading' element={<LoadingScreen/>}></Route>
    <Route exact path='/ListJobs' element={<ListJobs/>}></Route>
  </Routes>
  );
}

export default Main;