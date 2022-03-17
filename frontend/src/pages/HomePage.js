import '../App.css';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import mammoth from "mammoth/mammoth.browser";
import {useNavigate} from 'react-router-dom'; 



function HomePage() {

  const [file, setSelectedFile] = useState("");
  const [title, setTitle] = useState("");
  const [wholeText, setText] = useState("");
  const [city, setCity] = useState("");
  const [country, setCountry] = useState(""); 
  const navigate = useNavigate(); 

  function navigateTo() {
    navigate('/ListJobs');
  }

  function extractTextFromDocx(arrayBuffer) {
    mammoth
      .extractRawText({ arrayBuffer })
      .then(result => {
        
        const text = result.value; 
        
        const messages = result.messages; 
        
        setText( text );

        console.log(text); 
      });
  }

  function validateFile(fileName) {
    
    let docxFileExtension = /(\.docx)/i;

    if(docxFileExtension.exec(fileName)) {

        return true; 
    }

    else{
        return false; 
    }

  }

  function handleFileChange(file) {
    
    setTitle( file.name );

    console.log("Recieved and processed file: " + title); 

    let isValidFile = validateFile(file.name); 

    if( isValidFile ) {
    
        const reader = new FileReader();
    
        reader.readAsArrayBuffer(file);
        
        reader.onload = e => {
            extractTextFromDocx(e.target.result);
        }
    }

    else {
        alert("File type not supported! Please convert to docx format")
    }

    
  }


  return (
    <div className="App">
      <header className="App-header">
      
      <h1>Upload Resume and find your most ideal job!</h1>

      <h4>Leverage the power of Machine Learning to Find your best matching job</h4>
      <Stack spacing={60} direction="row">
        <Button variant="contained">Contained</Button>        
        <Button variant="contained">Contained</Button>
        <Button variant="contained">Contained</Button>
      </Stack>

      <Button variant="contained" component="label"> Upload File
        <input type="file" onChange={(e) => handleFileChange(e.target.files[0])} hidden/>
      </Button>

      <Stack>
          <Button variant="contained" onClick={navigateTo}> Find Matching Jobs </Button>
      </Stack>

      </header>
    </div>
  );
}

export default HomePage;