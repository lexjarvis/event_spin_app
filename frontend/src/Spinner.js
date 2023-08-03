import React, { useState } from 'react';
import './Spinner.css';

const Spinner = ({ onSpin }) => {
  const [isSpinning, setIsSpinning] = useState(false);

  const handleSpin = () => {
    setIsSpinning(true);
    setTimeout(() => {
      setIsSpinning(false);
      onSpin(); // Call the onSpin callback after the spin animation is complete
    }, 3000); // Simulate a 3-second spin duration, adjust as needed
  };

  return (
    <div className="spinner">
      <div className={`wheel ${isSpinning ? 'spinning' : ''}`} onClick={handleSpin}>
        {/* <div className="triangle"></div>
        <div className="triangle"></div>
        <div className="triangle"></div>
        <div className="triangle"></div>
        <div className="triangle"></div>
        <div className="triangle"></div>
        <div className="triangle"></div>
        <div className="triangle"></div> */}
      <div className="spin-button" onClick={handleSpin}>Spin</div>
      </div>
    </div>
  );
};

export default Spinner;


