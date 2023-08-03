import React, { useState } from 'react';
import Spinner from './Spinner';
import EventPopup from './EventPopup';
import axios from 'axios';
import './Homepage.css'; 

const Homepage = () => {
  const [location, setLocation] = useState('');
  const [showPopup, setShowPopup] = useState(false);
  const [eventData, setEventData] = useState({});

  const handleLocationChange = (e) => {
    setLocation(e.target.value);
  };

  const handleSpinClick = () => {
    axios
      .post('http://localhost:8008/spin', { location })
      .then((response) => {
        setEventData(response.data);
      })
      .catch((error) => {
        console.error('Error fetching event:', error);
      })
      .finally(() => {
        setShowPopup(true);
      });
  };

  const handleClosePopup = () => {
    setShowPopup(false);
  };

  return (
    <div className="homepage">
      <header>
        <h1>Event Spin</h1>
      </header>
      <div className="body">
        <input
          type="text"
          placeholder="Enter your location..."
          value={location}
          onChange={handleLocationChange}
        />
        <Spinner onSpin={handleSpinClick} />
        {showPopup && <EventPopup eventData={eventData} onClose={handleClosePopup} />}
      </div>
    </div>
  );
};

export default Homepage;




















