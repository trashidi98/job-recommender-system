import React from 'react';
import Particles from 'react-tsparticles';

function ParticlesContainer({ jobTitle, company, score }) {
    return (
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
    ); 
}

export default ParticlesContainer; 

// <Particles params={{
//         fpsLimit: 30,
//         particles: {
//           color: {
//             value: "#9400D3"
//           },
//           links: {
//             enable: true,
//             color: "#9c4be7",
//             distance: 125
//           },
//           move: {
//             enable: true
//           }
//         }
//       }}/>      
//     <div style={{
//         position: "absolute",
//         fpsLimit: 30,
//         particles: {
//           color: {
//             value: "#9400D3"
//           },
//           links: {
//             enable: true,
//             color: "#9c4be7",
//             distance: 125
//           },
//           move: {
//             enable: true
//           }
//         }
//     }}></div>