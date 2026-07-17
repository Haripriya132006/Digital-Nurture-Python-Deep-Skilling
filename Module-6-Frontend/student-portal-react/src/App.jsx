// App.jsx
import { useState} from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import CoursesPage from './pages/CoursesPage';
import ProfilePage from './pages/ProfilePage';
import CourseDetailPage from './pages/CourseDetailPage';

function App() {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const isEnrolled = (course) => {
    return enrolledCourses.some(item => item.id === course.id);
  };

  const handleEnroll = (course) => {
    if (isEnrolled(course)) {
      alert("You are already enrolled in this course!");
      return;
    }
    alert("Enrolled successfully!");
    setEnrolledCourses([...enrolledCourses, course]);
  };

  const noOfEnrolled = enrolledCourses.length;

  return (
    <div style={appLayout}>
      {/* Header stays on all pages */}
      <Header siteName="Student Portal" enrolled={noOfEnrolled} />
      
      <main style={mainContent}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          
          {/* Pass enrollment state and handlers as props to the CoursesPage */}
          <Route 
            path="/courses" 
            element={
              <CoursesPage 
                handleEnroll={handleEnroll} 
                isEnrolled={isEnrolled} 
              />
            } 
          />
          
          {/* Pass enrolled courses list to the ProfilePage */}
          <Route 
            path="/profile" 
            element={
              <ProfilePage enrolledCourses={enrolledCourses} />
            } 
          />
          
          <Route 
            path="/courses/:courseId" 
            element={<CourseDetailPage handleEnroll={handleEnroll} />} 
          />
        </Routes>
      </main>

      <Footer />
    </div>
  );
}

// Layout styles
const appLayout = {
  display: 'flex',
  flexDirection: 'column',
  minHeight: '100vh',
};

const mainContent = {
  flex: 1,
  padding: '20px',
};

export default App;