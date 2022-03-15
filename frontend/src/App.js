import logo from './logo.svg';
import './App.css';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import mammoth from "mammoth/mammoth.browser";



function App() {

  const [file, setSelectedFile] = useState("");
  
  const [title, setTitle] = useState("");
  const [wholeText, setText] = useState("");

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
      
      <Stack spacing={60} direction="row">
        <Button variant="contained">Contained</Button>        
        <Button variant="contained">Contained</Button>
        <Button variant="contained">Contained</Button>
      </Stack>


      <Button variant="contained" component="label"> Upload File
        <input type="file" onChange={(e) => handleFileChange(e.target.files[0])} hidden/>
      </Button>

      </header>
    </div>
  );
}

export default App;