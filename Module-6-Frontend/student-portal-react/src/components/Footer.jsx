// import React from 'react';

const Footer = () => {
          return (
          <footer style={footerStyle}>
                    <p>&copy; {new Date().getFullYear()} Student Portal. All rights reserved.</p>
          </footer>
          );
};

const footerStyle = {
          textAlign: 'center',
          padding: '15px',
          backgroundColor: '#f1f1f1',
          color: '#333',
          marginTop: '20px',
};

export default Footer;