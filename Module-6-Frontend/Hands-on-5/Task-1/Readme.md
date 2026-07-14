![alt text](<Screenshot 2026-07-14 203109.png>)
![alt text](<Screenshot 2026-07-14 214240.png>)

```
// import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';

function App() {
  return (
    <div style={appLayout}>
      <Header siteName="Student Portal" />
      
      <main style={mainContent}>
        <h2>My Enrolled Courses</h2>
        
        <div style={cardGrid}>
          <CourseCard
            name="Theory of Computation"
            code="CS301"
            credits={4}
            grade="A"
          />
          <CourseCard
            name="Compiler Construction"
            code="CS302"
            credits={4}
            grade="A"
          />
          <CourseCard
            name="Database Management Systems"
            code="CS303"
            credits={3}
            grade="B"
          />
        </div>
      </main>

      <Footer />
    </div>
  );
}

// Layout styling to make the footer stick to the bottom if content is short
const appLayout = {
  display: 'flex',
  flexDirection: 'column',
  minHeight: '100vh',
  fontFamily: 'Arial, sans-serif',
};

const mainContent = {
  flex: 1,
  padding: '20px',
  backgroundColor: '#f9f9f9',
};

const cardGrid = {
  display: 'flex',
  flexWrap: 'wrap',
  gap: '15px',
  marginTop: '15px',
};

export default App;
```