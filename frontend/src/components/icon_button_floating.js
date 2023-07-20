import React from 'react';
import './Image.css'; // Replace with the actual path to your CSS file

const Image = ({ src, alt }) => {
  return <img className="image" src={src} alt={alt} />;
};

export default Image;
