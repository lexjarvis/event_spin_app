import React from 'react';

const EventPopup = ({ eventData, onClose }) => {
  return (
    <div className="event-popup">
      {/* Popup content */}
      <div className="event-details">
        <img src={eventData.event_image} alt="Event" />
        <h2>{eventData.event_title}</h2>
        <p>{eventData.event_location}</p>
        <p>{eventData.event_date.when}</p>
        <a href={eventData.event_link} target="_blank" rel="noopener noreferrer">
          Learn More
        </a>
      </div>
      <button onClick={onClose}>Close</button>
    </div>
  );
};

export default EventPopup;
