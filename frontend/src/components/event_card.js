import React from 'react';
import './EventCard.css'; // Replace with the actual path to your CSS file
import EventCardDetails from './EventCardDetails'; // Import EventCardDetails component

const EventCard = ({ event }) => {
  return (
    <div className="event-card">
      {/* Render event card contents here */}
      <EventCardDetails details={event.details} />
    </div>
  );
};

export default EventCard;
