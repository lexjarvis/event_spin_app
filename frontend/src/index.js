import React, { useState } from 'react';
import axios from 'axios';

const HomePage = () => {
  const [zipCode, setZipCode] = useState('');
  const [searchRadius, setSearchRadius] = useState('');
  const [eventDate, setEventDate] = useState('');

  const handleSearch = async () => {
    try {
      // Construct the API request parameters
      const apiParams = {
        engine: 'google_events',
        q: 'Events in ' + zipCode,
        hl: 'en',
        gl: 'us',
        api_key: 'YOUR_SERP_API_KEY', // Replace with your actual SERP API key
      };
  
      // Make the API request to the backend
      const response = await axios.get('/api/events', { params: apiParams });
  
      // Extract the event data from the response
      const eventData = response.data;
  
      // Navigate to the second page with the fetched event data
      // For example, you can use React Router to navigate to the second page:
      // history.push('/second-page', { eventData });
    } catch (error) {
      console.error('Error fetching event data:', error);
    }
  };  

  return (
    <div>
      {/* Logo and Header */}
      <div>
        <img src="path_to_logo.png" alt="Logo" />
        <h1>Header Title</h1>
      </div>

      {/* Search Form */}
      <div>
        {/* Zip Code */}
        <input
          type="text"
          value={zipCode}
          onChange={(e) => setZipCode(e.target.value)}
          placeholder="Enter Zip Code"
        />

        {/* Search Radius */}
        <input
          type="text"
          value={searchRadius}
          onChange={(e) => setSearchRadius(e.target.value)}
          placeholder="Enter Search Radius"
        />

        {/* Date Picker */}
        <input
          type="date"
          value={eventDate}
          onChange={(e) => setEventDate(e.target.value)}
        />

        {/* Search Button */}
        <button onClick={handleSearch}>Search</button>
      </div>
    </div>
  );
};

export default HomePage;

