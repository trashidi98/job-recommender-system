import Stack from '@mui/material/Stack';
import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import './OutlinedCard.css'



function OutlinedCard({ jobTitle, company, score }) {

  return (

    <Box sx={{ minWidth: 1000 }}>

      <Card variant="outlined">

        <CardContent>
          <div className='inside-card'>
            <div>
              <h4>{jobTitle}</h4>
            </div>

            <div>
              <h4>{company}</h4>
            </div>

            <div>
              <h4>{score}</h4>
            </div>
          </div>
        </CardContent>

      </Card>

    </Box>

  );
}

export default OutlinedCard; 
