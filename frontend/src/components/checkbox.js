import React from 'react';
import './Checkbox.css'; // Replace with the actual path to your CSS file

const Checkbox = ({ label, checked, onChange }) => {
  return (
    <label className="checkbox">
      <input type="checkbox" checked={checked} onChange={onChange} />
      {label}
    </label>
  );
};

export default Checkbox;
