
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








