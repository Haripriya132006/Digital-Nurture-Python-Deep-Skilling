import {Link} from 'react-router-dom';
// import { useContext } from 'react';
// import { EnrollmentContext } from '../EnrollmentContext';

import { useSelector } from 'react-redux';
const Header = (props) => {
          const enrolledCourses=useSelector((state)=>state.enrollment.enrolledCourses);
          return (
          <>
          <header style={headerStyle}>
                    <h1>{props.siteName}</h1>
                    <nav>
                              <ul style={navLinksStyle}>
                                        <li><Link to="#home">Home</Link></li>
                                        <li><Link to="#courses">Courses</Link></li>
                                        <li><Link to="#profile">Profile</Link></li>
                              </ul>
                    </nav>
          </header>
          <h3>Number of Courses Enrolled: {enrolledCourses.length}</h3>
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