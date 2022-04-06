import '../App.css';
import './HomePage.css';
import Cookies from 'js-cookie';
import Button from '@mui/material/Button';
import React, { useState } from 'react';
import mammoth from "mammoth/mammoth.browser";
import { useNavigate } from 'react-router-dom';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import TextInput from 'react-autocomplete-input';
import { MuiThemeProvider, createTheme, useTheme } from '@material-ui/core/styles';
import Particles from "react-tsparticles";


import { cities } from '../data/cities';
import axios from 'axios'; 
axios.defaults.withCredentials = true;


const theme = createTheme({
  palette: {
    text: {
      primary: '#9200D1',
      secondary: '#9200D1',
    },
  },
});


function HomePage() {

  const [file, setSelectedFile] = useState("");
  const [title, setTitle] = useState("");
  const [wholeText, setText] = useState(""); 
  const [backendData, setBackendData] = useState(""); 
  var city = "";

  const navigate = useNavigate();

  const csrftoken = Cookies.get('csrftoken') // Cookies from Django Domain

  const loginRequest = async (resume_text, city) => {
      await axios({
          method: "post",
          url: `http://127.0.0.1:8000/api/v1/userresume`,
          headers: { 'X-CSRFToken': csrftoken },
          data: {
            'resume_text': resume_text,
            'city': city
          }
      }).then((res) => {
          setBackendData(res.data); 
          console.log(res.data);
      })
  }

  function navigateTo() {
    navigate('/ListJobs', {state: backendData});
  }

  function extractTextFromDocx(arrayBuffer) {
    mammoth
      .extractRawText({ arrayBuffer })
      .then(result => {
        const text = result.value;
        setText(text);
        loginRequest(result.value, city)
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

  function handleCityChange(thisCity) {
    city = thisCity;
    console.log(city); 
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
         
      <Particles params={{
      fpsLimit: 30,
      particles: {
        color: {
          value: "#9400D3"
        },
        links: {
          enable: true,
          color: "#9c4be7",
          distance: 125
        },
        move: {
          enable: true
        }
      }
    }}/>      
  <div style={{
      position: "absolute",
      fpsLimit: 30,
      particles: {
        color: {
          value: "#9400D3"
        },
        links: {
          enable: true,
          color: "#9c4be7",
          distance: 125
        },
        move: {
          enable: true
        }
      }
  }}>

        <div className="HomePage">
          <h2>Leverage the power of ML to find your tech job</h2>
            
            <h5> 1. Filter by a city <br></br>              
            </h5>
            <div className='white-text'>
            <Autocomplete
                disablePortal
                id="combo-box-demo"
                options={cities}
                sx={{backgroundColor: 'rgba(148, 0, 211, 0.7)', borderRadius: '10px',
                '& label.Mui-focused': {
                  color: 'white',
                },
                '& .MuiInput-underline:after': {
                  borderBottomColor: 'white',
                },
                '& .MuiOutlinedInput-root': {
                    color: 'white',
                  '& fieldset': {
                    borderColor: 'black',
                  },
                  '&.Mui-focused fieldset': {
                    borderColor: 'white',
                  },
                }
                }}
                variant="contained"
                onChange={ (event, value) => { handleCityChange(value.label) }} 
                renderInput={(params) => <TextField {...params} label="Cities"/>} />
            </div>
            <h5>2. Upload your resume in .docx format. <br></br>
              <Button variant="contained" component="label" style={{ borderRadius: 12, backgroundColor: "rgba(148, 0, 211, 0.9)", height: '70px', width : '400px'}}>
                Upload File (.docx)
                <input type="file" onChange={(e) => handleFileChange(e.target.files[0])} hidden />
              </Button>
            </h5>
            
            <h5>3. Discover your most ideal jobs<br></br>
            <Button variant="contained" component="label" onClick={navigateTo} style={{
                    borderRadius: 12,
                    backgroundColor: "rgba(148, 0, 211, 0.9)",
                    height: '70px', 
                    width : '400px'
                }}> Find Matching Jobs 
            </Button>
            </h5>
          </div>
          
          </div>
      </header>
    </div>
  );
}

export default HomePage;