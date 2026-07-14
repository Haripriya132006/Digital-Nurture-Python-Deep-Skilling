// import React from 'react';

const Header = (props) => {
          return (
          <>
          <header style={headerStyle}>
                    <h1>{props.siteName}</h1>
                    <nav>
                              <ul style={navLinksStyle}>
                                        <li><a href="#home">Home</a></li>
                                        <li><a href="#courses">Courses</a></li>
                                        <li><a href="#profile">Profile</a></li>
                              </ul>
                    </nav>
          </header>
          <h3>Number of Courses Enrolled: {props.enrolled}</h3>
          </>
          );
};

// Simple inline styles for presentation
const headerStyle = {
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
};

const navLinksStyle = {
          display: 'flex',
          listStyle: 'none',
          gap: '15px',
          margin: 0,
          padding: 0,
};

export default Header;