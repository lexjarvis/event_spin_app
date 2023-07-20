import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './DatePicker.css'; // Replace with the actual path to your CSS file

const CustomDatePicker = ({ selectedDate, onChange }) => {
  // State to manage the date value
  const [date, setDate] = useState(selectedDate);

  // Handle date change
  const handleDateChange = (newDate) => {
    setDate(newDate);
    // Pass the new date value to the parent component
    onChange(newDate);
  };

  return (
    <DatePicker
      selected={date}
      onChange={handleDateChange}
      dateFormat="yyyy-MM-dd"
      className="custom-datepicker"
    />
  );
};

export default CustomDatePicker;
