import '../App.css';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import React, { useState } from 'react';
import { Component} from 'react';
import mammoth from "mammoth/mammoth.browser";
import { useNavigate } from 'react-router-dom';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { cities } from '../data/cities';
import axios from "axios";

class HomePage extends Component {

  state = {
    resume: '',
    filename: '',
    filetype: false, 
  }

  extractTextFromDocx = (arrayBuffer) =>{
    mammoth
      .extractRawText({ arrayBuffer })
      .then(result => {
        const text = result.value
        //const messages = result.messages
        this.setState({resume: text})
        axios.post(`http://127.0.0.1:8000/api/v1/userresume`, 
        { 'user_resume': this.state.resume })
      .then(res => {
        console.log(res)
        console.log(res.data)
      })
        console.log(this.state.resume)
      })
  }

  validateFile = (fileName) => {

    let docxFileExtension = /(\.docx)/i
    if (docxFileExtension.exec(this.state.filename)) {
      this.setState({ filetype: true})
    } else {
      this.setState({ filetype: false})}
  }

  handleFileChange = (file) => {

    this.setState({ filename: file.name})
    console.log("Recieved and processed file: " + this.state.filename)
    this.validateFile(this.state.filename)

    if (this.state.filetype=true) {
      const reader = new FileReader()
      reader.readAsArrayBuffer(file)
      reader.onload = e => {
        this.extractTextFromDocx(e.target.result)
      }} else {
      alert("File type is not supported! Please convert to docx format")
    }
  }
  

  render() { 
      return (
        <div className="App">
          <header className="App-header">

            <h1>Upload Resume and find your most ideal job!</h1>

            <h4>Leverage the power of machine learning to find your best matching job</h4>
            <Autocomplete
              disablePortal
              id="combo-box-demo"
              options={cities}
              sx={{ width: 300 }}
              renderInput={(params) => <TextField {...params} label="Cities" />} />

            <Button variant="contained" component="label"> Upload File
              <input type="file" onChange={(e) => this.handleFileChange(e.target.files[0])} hidden />
            </Button>

          </header>
        </div>
      )
    }
  }
}

export default HomePage