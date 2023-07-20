import React from 'react';
import './Button.css'; // Replace with the actual path to your CSS file

const Button = ({ label, onClick }) => {
  return (
    <button className="button" onClick={onClick}>
      {label}
    </button>
  );
};

export default Button;
