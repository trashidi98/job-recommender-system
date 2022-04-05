import Stack from '@mui/material/Stack';
import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CountUp from 'react-countup';
import './OutlinedCard.css'
import Modal from '@mui/material/Modal';
import ButtonBase from '@material-ui/core/ButtonBase';

import Backdrop from '@mui/material/Backdrop';
import Fade from '@mui/material/Fade';


function OutlinedCard({ jobTitle, company, score }) {
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
        <Card variant="outlined" style={{ backgroundColor: 'rgba(148, 0, 211, 0.7)' }}>
          <CardContent>
            <div className='inside-card'>
              <div>
                <h4>{jobTitle}</h4>
              </div>

              <div>
                <h4>{company}</h4>
              </div>

              <div>
                <CountUp end={score} useEasing={true} duration={4} />
              </div>

              <CardActions>

                <Button onClick={handleOpen}>Description</Button>
                <Modal
                  aria-labelledby="transition-modal-title"
                  aria-describedby="transition-modal-description"
                  open={open}
                  onClose={handleClose}
                  closeAfterTransition
                  BackdropComponent={Backdrop}
                  BackdropProps={{
                    timeout: 500,
                  }}
                >
                  <Fade in={open}>
                    <Box sx={style}>
                      <Typography id="transition-modal-title" variant="h6" component="h2">
                        Text in a modal
                      </Typography>
                      <Typography id="transition-modal-description" sx={{ mt: 2 }}>
                        Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
                      </Typography>
                    </Box>
                  </Fade>
                </Modal>
              </CardActions>

            </div>
          </CardContent>
        </Card>
      </div>
    </Box>

  );
}

export default OutlinedCard; 