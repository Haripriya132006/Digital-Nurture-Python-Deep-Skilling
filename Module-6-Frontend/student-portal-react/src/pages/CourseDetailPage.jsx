// src/pages/CourseDetailPage.jsx
// import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';

function CourseDetailPage({ handleEnroll }) {
  const { courseId } = useParams();
  const navigate = useNavigate();

  // Mock data to display the course details based on the URL ID
  const coursesData = {
    "1": { name: "Python", code: "IT101", credits: 3, description: "Learn the basics of Python programming, loops, and data structures." },
    "2": { name: "System Design", code: "CS101", credits: 4, description: "Understand how to design scalable, reliable, and maintainable systems." },
    "3": { name: "Web Designing", code: "IT201", credits: 5, description: "HTML, CSS, and modern UI/UX design concepts." },
    "4": { name: "Database Management System", code: "CS201", credits: 3, description: "SQL, normalization, indexing, and relational database concepts." },
    "5": { name: "Spring Boot", code: "IT301", credits: 4, description: "Build enterprise-grade Java backend applications using Spring Boot." }
  };

  const course = coursesData[courseId];

  const onEnrollClick = () => {
    if (course) {
      handleEnroll(course);
      navigate('/profile'); // Automatically go to profile after enrolling (Step 80)
    }
  };

  if (!course) {
    return (
      <div style={{ padding: '20px' }}>
        <h2>Course not found!</h2>
        <button onClick={() => navigate('/courses')} style={buttonStyle}>
          Back to Courses
        </button>
      </div>
    );
  }

  return (
    <div style={containerStyle}>
      <h2>{course.name}</h2>
      <p><strong>Code:</strong> {course.code}</p>
      <p><strong>Credits:</strong> {course.credits}</p>
      <p><strong>Description:</strong> {course.description}</p>
      
      <div style={{ display: 'flex', gap: '10px', marginTop: '20px' }}>
        <button onClick={onEnrollClick} style={enrollButtonStyle}>
          Enroll in Course
        </button>
        <button onClick={() => navigate('/courses')} style={buttonStyle}>
          Back to Courses
        </button>
      </div>
    </div>
  );
}

// Simple Inline Styles
const containerStyle = {
  padding: '20px',
  border: '1px solid #ccc',
  borderRadius: '8px',
  maxWidth: '600px',
  margin: '20px auto',
  backgroundColor: '#f9f9f9',
};

const enrollButtonStyle = {
  padding: '10px 15px',
  backgroundColor: '#28a745',
  color: 'white',
  border: 'none',
  borderRadius: '4px',
  cursor: 'pointer',
};

const buttonStyle = {
  padding: '10px 15px',
  backgroundColor: '#007bff',
  color: 'white',
  border: 'none',
  borderRadius: '4px',
  cursor: 'pointer',
};

// This is the default export that App.jsx was looking for!
export default CourseDetailPage;