import React, { useState } from 'react';
import './Spinner.css';

const Spinner = ({ onSpin }) => {
  const [isSpinning, setIsSpinning] = useState(false);

  const handleSpin = () => {
    setIsSpinning(true);
    setTimeout(() => {
      setIsSpinning(false);
      onSpin(); 
    }, 3000); 
  };

  return (
    <div className="spinner">
      <div className={`wheel ${isSpinning ? 'spinning' : ''}`} onClick={handleSpin}>
      <div className="spin-button" onClick={handleSpin}>SPIN</div>
      </div>
    </div>
  );
};

export default Spinner;


