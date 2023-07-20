import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    // Fetch data from the backend API endpoint
    axios.get('http://127.0.0.1:8008/events')
      .then(response => {
        setEvents(response.data); // Assuming the response contains an array of events
      })
      .catch(error => {
        console.error('Error fetching events:', error);
      });
  }, []);

  return (
    <div>
      {/* Display the events fetched from the backend */}
      {events.map(event => (
        <div key={event.id}>
          <h2>{event.event_name}</h2>
          <p>{event.event_summary}</p>
          {/* Add more event details here */}
        </div>
      ))}
    </div>
  );
}

export default App;

