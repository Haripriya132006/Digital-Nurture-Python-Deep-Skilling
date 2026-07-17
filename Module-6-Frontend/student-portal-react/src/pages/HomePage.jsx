// pages/HomePage.jsx
// import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div style={{ textAlign: 'center', padding: '40px 20px' }}>
      <h1>Welcome to the Student Portal!</h1>
      <p>Manage your classes, track your grades, and explore new learning opportunities.</p>
      <Link to="/courses" style={{ display: 'inline-block', marginTop: '20px', padding: '10px 20px', backgroundColor: '#007bff', color: 'white', textDecoration: 'none', borderRadius: '5px' }}>
        Browse Courses
      </Link>
    </div>
  );
}

export default HomePage;