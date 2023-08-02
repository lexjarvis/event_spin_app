import React, { useState } from 'react';
import Spinner from './Spinner';
import EventPopup from './EventPopup';
import axios from 'axios';
import './Homepage.css'; // Import the CSS file

const Homepage = () => {
  const [location, setLocation] = useState('');
  const [showPopup, setShowPopup] = useState(false);
  const [eventData, setEventData] = useState({});

  const handleLocationChange = (e) => {
    setLocation(e.target.value);
  };

  const handleSpinClick = () => {
    axios
      .post('http://localhost:8008/spin', { location }) // Adjust the URL to your backend server URL
      .then((response) => {
        setEventData(response.data);
        setShowPopup(true);
      })
      .catch((error) => {
        console.error('Error fetching event:', error);
        // Optionally, show an error message to the user.
      });
  };

  const handleClosePopup = () => {
    setShowPopup(false);
  };

  return (
    <div className="homepage">
      <header>
        {/* Your logo here */}
        <h1>EventSpin</h1>
      </header>
      <div className="body">
        <input
          type="text"
          placeholder="Enter your location..."
          value={location}
          onChange={handleLocationChange}
        />
        <button onClick={handleSpinClick}>Spin</button>
        <Spinner />
      </div>
      {showPopup && <EventPopup eventData={eventData} onClose={handleClosePopup} />}
    </div>
  );
};

export default Homepage;

 






