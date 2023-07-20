import React, { useState } from 'react';
import { Link, useHistory } from 'react-router-dom';

const HomePage = () => {
  const history = useHistory();
  const [formData, setFormData] = useState({
    zipCode: '',
    searchRadius: '',
    eventDate: null,
    morning: false,
    afternoon: false,
    evening: false,
    free: false,
    ageRestricted: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSearch = () => {
    // Perform any necessary validation on form data before navigating to the second page
    history.push('/second-page', formData);
  };

  return (
    <div>
      <header>
        <img src="/path/to/logo.png" alt="Logo" />
        <h1>Header Text</h1>
      </header>
      <form>
        {/* Zip Code text field */}
        <input
          type="text"
          name="zipCode"
          value={formData.zipCode}
          onChange={handleChange}
          placeholder="Enter Zip Code"
        />
        {/* Search Radius (miles) text field */}
        <input
          type="text"
          name="searchRadius"
          value={formData.searchRadius}
          onChange={handleChange}
          placeholder="Enter Search Radius (miles)"
        />
        {/* Date Picker field */}
        {/* Implement your date picker component here */}
        <p>Only show events that are:</p>
        {/* Checkboxes */}
        <label>
          <input
            type="checkbox"
            name="morning"
            checked={formData.morning}
            onChange={handleChange}
          />
          in the morning
        </label>
        {/* Add other checkboxes here */}
        {/* Search Button */}
        <button type="button" onClick={handleSearch}>
          Search
        </button>
      </form>
    </div>
  );
};

export default HomePage;
