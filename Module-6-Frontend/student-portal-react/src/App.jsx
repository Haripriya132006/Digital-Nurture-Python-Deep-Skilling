// import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import { useState } from 'react';
function App() {
  const courses=[
    {id:1,name:"Python",code:"IT101",credits:3,grade:"A"},
    {id:2,name:"System Design",code:"CS101",credits:4,grade:"A"},
    {id:3,name:"Web Designing",code:"IT201",credits:5,grade:"A"},
    {id:4,name:"Database Management System",code:"CS201",credits:3,grade:"A"},
    {id:5,name:"Spring Boot",code:"IT301",credits:4,grade:"A"},
    
  ]
  const [searchTerm,setSerchTerm]=useState('');

  const filteredCourses=courses.filter(course=>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  )
  
  const [enrolledCourses,setEnrolledCourses]=useState([]);

  const isEnrolled=(course)=>{
    return enrolledCourses.some(item=>item.id===course.id);
  }

  const handleEnroll=(course)=>{
    if(enrolledCourses.some(item=>item.id===course.id)){
      alert("You are already enrolled in this course!");
      return;
    }
    alert("enrolled successfully")
    setEnrolledCourses([...enrolledCourses,course]);
    
  }
const noOfEnrolled=enrolledCourses.length;

  return (
    <div style={appLayout}>
      <Header siteName="Student Portal" enrolled={noOfEnrolled} />
      
      <main style={mainContent}>
        <h2>My Enrolled Courses</h2>
        <input type='text' value={searchTerm} placeholder='search'
        onChange={(e)=>setSerchTerm(e.target.value)}/>

        <div style={cardGrid}>
          {filteredCourses.map(course => {
          return (<CourseCard
            key={course.id}
            name={course.name}
            code={course.code}
            credits={course.credits}
            grade={course.grade}
            onEnroll={()=>handleEnroll(course)}
            isEnrolled={isEnrolled(course)}
          />);
          })}
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