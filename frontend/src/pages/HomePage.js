import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

const HomePage = () => {
  const [selectedEvent, setSelectedEvent] = useState(null);
  const history = useHistory();

  const handleSpin = () => {
    // Make API request to fetch event data based on user inputs
    // Once you have the randomly selected event data, set it in the state
    // For example:
    // const randomlySelectedEvent = ...; // Get the randomly selected event from the fetched event data
    // setSelectedEvent(randomlySelectedEvent);

    // Redirect to the EventListPage and pass the selectedEvent as a URL parameter
    history.push('/event-list', { selectedEvent });
  };

  return (
    <div>
      {/* Logo and Header */}
      {/* Search Form */}
      {/* ... */}
      <button onClick={handleSpin}>Spin</button>
    </div>
  );
};

export default HomePage;


