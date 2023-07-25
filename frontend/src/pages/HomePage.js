// create a component for this page that contains the logo, header and search form
// the search form will contain these fields: zip code, search radius, date picker, checkboxes and search button
// handle user inputs using React state
// when the search button is clicked, make an API request to backend to fetch event data based on user's input

import React, { useState } from 'react';

const HomePage = () => {
  const [zipCode, setZipCode] = useState('');
  const [searchRadius, setSearchRadius] = useState('');
  const [eventDate, setEventDate] = useState('');
  const [timePreference, setTimePreference] = useState([]);
  const [freeEventsOnly, setFreeEventsOnly] = useState(false);
  const [ageRestricted, setAgeRestricted] = useState(false);

  const handleSearch = () => {
    // Make API request to fetch event data based on user inputs
    // Navigate to the second page with the fetched event data
  };

  return (
    <div>
      {/* Logo and Header */}
      {/* Search Form */}
      {/* Zip Code */}
      {/* Search Radius */}
      {/* Date Picker */}
      {/* Time Preference Checkboxes */}
      {/* Free and Age Restricted Checkboxes */}
      {/* Search Button */}
    </div>
  );
};

export default HomePage;
