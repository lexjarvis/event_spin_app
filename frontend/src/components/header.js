import React from 'react';
import './Header.css'; // Replace with the actual path to your CSS file

const Header = ({ title }) => {
  return (
    <header className="header">
      <h1>{title}</h1>
    </header>
  );
};

export default Header;
