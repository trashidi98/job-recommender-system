import Stack from '@mui/material/Stack';
import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import './OutlinedCard.css'



function OutlinedCard({jobTitle, company, score}) {

  return (
     
     <Box sx={{ minWidth: 1000 }}>

     <Card variant="outlined">
     
      <CardContent>

        <Stack direction="row" spacing={110}>
            
            <div>
              <h4>{jobTitle}</h4>
            </div>

            <div>
              <h4>{company}</h4>
            </div>

            <div>
              <h4>{score}</h4>
            </div>

        </Stack>

      </CardContent>
     </Card>
    </Box>

  ); 
}

export default OutlinedCard; 

// const card = (
//   <React.Fragment>
    
//     <CardContent>

//     <Stack direction="row" spacing={110}>
        
//         <div>
//           <h4>Job Title</h4>
//         </div>

//         <div>
//           <h4>Company</h4>
//         </div>

//         <div>
//           <h4>Percentage</h4>
//         </div>

//       </Stack>

//     </CardContent>
    
//   </React.Fragment>
// );

// export default function OutlinedCard() {
//   return (
//     <Box sx={{ minWidth: 1000 }}>
//       <Card variant="outlined">{card}</Card>
//     </Box>
//   );
// }
