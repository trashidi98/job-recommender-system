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
 
//   function getSelectedFile(eventFileBlob) {
//     console.log(eventFileBlob);


//     var reader = new FileReader();
//     reader.readAsArrayBuffer(eventFileBlob);

//     reader.onload = (e) => {
//         console.log(e.target.result);
//         var enc = new TextDecoder("utf-8");

//         console.log(enc.decode(e.target.result));
    
//         var mam = mammoth.extractRawText(e.target.result);

//         console.log(mam); 
//     }
//   }

    // reader.onload = () => {
    //     extractRawText({ eventFileBlob })
    //         .then(result => {console.log(result.value)})
    // }}


  function extractWordRawText(arrayBuffer) {
    mammoth
      .extractRawText({ arrayBuffer })
      .then(result => {
        const text = result.value; // The raw text
        const messages = result.messages; // Please handle messages
        setText( text );

        console.log(text); 
      })
      .done();


  };

  function handleFileChange(file) {
    const reader = new FileReader();
    reader.readAsArrayBuffer(file);
    reader.onload = e => {
      extractWordRawText(e.target.result);
    };

    setTitle( file.name );
  };


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