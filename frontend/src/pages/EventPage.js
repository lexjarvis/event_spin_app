import React, { useEffect, useState } from 'react';
import { useLocation, useHistory } from 'react-router-dom';

const EventListPage = () => {
  const location = useLocation();
  const history = useHistory();
  const [selectedEvent, setSelectedEvent] = useState(null);

  useEffect(() => {
    // Extract the selectedEvent from the URL parameters
    if (location.state && location.state.selectedEvent) {
      setSelectedEvent(location.state.selectedEvent);
    } else {
      // If the selectedEvent is not available in the URL parameters, redirect back to the homepage
      history.push('/');
    }
  }, [location.state, history]);

  const handlePopupClose = () => {
    // Close the popup and redirect back to the homepage
    history.push('/');
  };

  return (
    <div>
      {/* Logo and Header */}
      {/* Back Arrow Button */}
      {/* Spin Wheel */}

      {selectedEvent && (
        /* Popup with Event Details */
        <div>
          {/* Event Image */}
          <img src={selectedEvent.event_image} alt="Event" />

          {/* Event Title */}
          <h2>{selectedEvent.event_title}</h2>

          {/* Event Summary */}
          <p>{selectedEvent.event_summary}</p>

          {/* Event Location */}
          <p>Location: {selectedEvent.event_location}</p>

          {/* Event Date */}
          <p>Date: {selectedEvent.event_date}</p>

          {/* Event Start Time */}
          <p>Start Time: {selectedEvent.event_start_time}</p>

          {/* Event End Time */}
          <p>End Time: {selectedEvent.event_end_time}</p>

          {/* Visit Full Event Page Button */}
          <a href={selectedEvent.event_link} target="_blank" rel="noopener noreferrer">
            Visit Full Event Page
          </a>

          {/* Close Popup Button */}
          <button onClick={handlePopupClose}>Close</button>
        </div>
      )}
    </div>
  );
};

export default EventListPage;



