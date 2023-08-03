// import React from 'react';
// import EventSpin from './Homepage';

// function App() {
//   return (
//     <div className="App">
//       <EventSpin />
//     </div>
//   );
// }

// export default App;

// import React from 'react';
// import './App.css';
// import Homepage from './Homepage';

// function App() {
//   return (
//     <div className="App">
//       <Homepage />
//     </div>
//   );
// }

// export default App;

// import React, { useState } from 'react';
// import './App.css';
// import Homepage from './Homepage';
// import EventPopup from './EventPopup';


// function App() {
//   const handleSpinComplete = () => {
//     // Handle the event popup generation here
//     // For example, you can set the state to show the event popup component
//   };

//   return (
//     <div className="App">
//       <Homepage onSpinComplete={handleSpinComplete} /> {/* Update prop name here */}
//     </div>
//   );
// }

// export default App;

import React, { useState } from 'react';
import './App.css';
import Homepage from './Homepage';
import EventPopup from './EventPopup';

function App() {
  const [showPopup, setShowPopup] = useState(false);
  const [eventData, setEventData] = useState({});

  const handleSpinComplete = (data) => {
    setEventData(data);
    setShowPopup(true);
  };

  const handleClosePopup = () => {
    setShowPopup(false);
  };

  return (
    <div className="App">
      <Homepage onSpinComplete={handleSpinComplete} />
      {showPopup && <EventPopup eventData={eventData} onClose={handleClosePopup} />}
    </div>
  );
}

export default App;








