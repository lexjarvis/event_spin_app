import React from 'react';
import './Field.css'; // Replace with the actual path to your CSS file

const Field = ({ label, value, onChange }) => {
  return (
    <div className="field">
      <label>{label}</label>
      <input type="text" value={value} onChange={onChange} />
    </div>
  );
};

export default Field;
