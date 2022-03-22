import '../App.css';
import Cookies from 'js-cookie';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import mammoth from "mammoth/mammoth.browser";
import { useNavigate } from 'react-router-dom';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { cities } from '../data/cities';
import axios from 'axios'; 
axios.defaults.withCredentials = true;

function HomePage() {

  const [file, setSelectedFile] = useState("");
  const [title, setTitle] = useState("");
  const [wholeText, setText] = useState("");
  const [city, setCity] = useState("");
  const [country, setCountry] = useState("");
  const navigate = useNavigate();

  const csrftoken = Cookies.get('csrftoken') // Cookies from Django Domain

  const loginRequest = async (e) => {
      await axios({
          method: "post",
          url: `http://127.0.0.1:8000/api/v1/userresume`,
          headers: { 'X-CSRFToken': csrftoken },
          data: {'resume_text': e}
      }).then((res) => {
          console.log(res.data);
      })
  }

  function navigateTo() {
    navigate('/ListJobs');
  }

  function extractTextFromDocx(arrayBuffer) {
    mammoth
      .extractRawText({ arrayBuffer })
      .then(result => {
        const text = result.value;
        const messages = result.messages;
        setText(text);
        loginRequest(result.value)
      });
  }

  function validateFile(fileName) {

    let docxFileExtension = /(\.docx)/i;

    if (docxFileExtension.exec(fileName)) {

      return true;
    }

    else {
      return false;
    }

  }

  function handleFileChange(file) {

    setTitle(file.name);

    console.log("Recieved and processed file: " + title);

    let isValidFile = validateFile(file.name);

    if (isValidFile) {

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
        <h2>Leverage the power of ML and your resume to find your most ideal job!</h2>
      
        {/* <h4>Leverage the power of machine learning recommender systems to find the best matching jobs</h4> */}
          <h5> 1. Filter by a city. (Optional) 
            <Autocomplete
              disablePortal
              id="combo-box-demo"
              variant="contained"
              options={cities}
              sx={{ width: 300 }}
              renderInput={(params) => <TextField {...params} label="Cities" />} /> 
          </h5>
          
          <h5>2. Upload your resume in .docx format. <br></br>
            <Button variant="contained" component="label" style={{height: '50px', width : '300px'}}>
              Upload File (.docx)
              <input type="file" onChange={(e) => handleFileChange(e.target.files[0])} hidden />
            </Button>
          </h5>
          
          <h5>3. Discover your most ideal jobs!<br></br>
            <Button variant="contained" component="label" onClick={navigateTo} style={{height: '50px', width : '300px'}}> Find Matching Jobs </Button>
          </h5>
      </header>
    </div>
  );
}

export default HomePage;