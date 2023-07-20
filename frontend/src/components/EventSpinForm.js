// src/components/EventSpinForm.js
import React, { useState } from 'react';
import { spinWheel } from '../api';

const EventSpinForm = () => {
  const [zipCode, setZipCode] = useState('');
  // Add state for other spin parameters

  const handleSpin = async () => {
    try {
      const spinParams = {
        zip_code: zipCode,
        // Add other spin parameters here
      };
      const eventData = await spinWheel(spinParams);
      // Update the state or handle the event data as needed
      console.log(eventData);
    } catch (error) {
      console.error('Error spinning wheel:', error);
    }
  };

  return (
    <div>
      <label htmlFor="zipCode">Zip Code:</label>
      <input
        type="text"
        id="zipCode"
        value={zipCode}
        onChange={(e) => setZipCode(e.target.value)}
      />
      {/* Add other input fields for spin parameters */}
      <button onClick={handleSpin}>Spin</button>
    </div>
  );
};

export default EventSpinForm;
