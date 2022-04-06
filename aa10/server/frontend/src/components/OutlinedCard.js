import Stack from '@mui/material/Stack';
import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import ButtonBase from '@material-ui/core/ButtonBase';
import Backdrop from '@mui/material/Backdrop';
import Fade from '@mui/material/Fade';
import CountUp from 'react-countup';
import {useNavigate, useLocation} from "react-router-dom"; 
import './OutlinedCard.css'


function OutlinedCard({ jobTitle, company, score, description }) {

  var location = useLocation(); 
  const navigate = useNavigate();

  function navigateForward() {
    navigate('/JobDescription', {state: [jobTitle, company, description]})
  }

  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };



  
  return (

    <Box sx={{ minWidth: 1000 }}>
      <div className="card-outline">
      <Card variant="outlined" style={{backgroundColor: 'rgba(148, 0, 211, 0.7)'} }>

        <CardContent>
          <div className='inside-card'>
            <div>
              <h4>{jobTitle}</h4>
            </div>

            <div>
              <h4>{company}</h4>
            </div>

            <div className="countup">
              <CountUp end={score} useEasing={true} duration={4}/>
            </div>

            <CardActions>
            <Button
                style={{
                    borderRadius: 12,
                    backgroundColor: "#9200D1",
                    fontSize: "calc(1px + 2vmin)"
                }}
                variant="contained"
                onClick={navigateForward}>
                Description
            </Button>
            </CardActions>     

          </div>
        </CardContent>
      </Card>
      </div>
    </Box>

  );
}

export default OutlinedCard; 