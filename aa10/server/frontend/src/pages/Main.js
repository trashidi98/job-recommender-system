import React from 'react';
import {Routes, Route} from 'react-router-dom';
import Axios from "axios";

import HomePage from './HomePage';
import ListJobs from './ListJobs';

const Main = () => {
  return (
    <Routes> {/* The Routes decides which component to show based on the current URL.*/}
      <Route exact path='/' element={<HomePage/>}></Route>
      <Route exact path='/ListJobs' element={<ListJobs/>}></Route>
    </Routes>
  );
}

export default Main;