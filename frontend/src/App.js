import logo from './logo.svg';
import './App.css';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';



function App() {

  const [file, setSelectedFile] = useState("");  
 
  function getSelectedFile(eventFileBlob) {
    setSelectedFile(eventFileBlob); 
    console.log(file);


    var reader = new FileReader();
    
  }


  return (
    <div className="App">
      <header className="App-header">
      
      <Stack spacing={60} direction="row">
        <Button variant="contained">Contained</Button>        
        <Button variant="contained">Contained</Button>
        <Button variant="contained">Contained</Button>
      </Stack>


      <Button variant="contained" component="label"> Upload File
        <input type="file" onChange={(e) => getSelectedFile(e.target.files[0])} hidden/>
      </Button>

      </header>
    </div>
  );
}

export default App;