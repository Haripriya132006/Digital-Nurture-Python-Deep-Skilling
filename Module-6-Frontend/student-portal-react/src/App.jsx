// import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';
import { useState } from 'react';
import {useEffect} from 'react';
function App() {
  const courses=[
    {id:1,name:"Python",code:"IT101",credits:3,grade:"A"},
    {id:2,name:"System Design",code:"CS101",credits:4,grade:"A"},
    {id:3,name:"Web Designing",code:"IT201",credits:5,grade:"A"},
    {id:4,name:"Database Management System",code:"CS201",credits:3,grade:"A"},
    {id:5,name:"Spring Boot",code:"IT301",credits:4,grade:"A"},
    
  ]
  const [searchTerm,setSerchTerm]=useState('');
  
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
  // -----------------------------------------------------
  const [newCourses,setNewCourses]=useState([]);
  const [loading,setLoading]=useState(true);
  const[error,setError]=useState(null);
  const merged=[...courses,...newCourses];
  
  useEffect(()=>{
    fetch('https://jsonplaceholder.typicode.com/posts')
    .then((response)=>{
      if(!response.ok){
        throw new Error('Failed to fetch courses data.');
      }
      return response.json();
    })
    .then((data)=>{
      const mapped=data.slice(0,5).map((post)=>({
        id:post.id+courses.length,
        name:post.title,
        code:`CS${post.id+400}`,
        credits:(post.id%2===0)?4:3,
        grade:'Pending'
      }));
      setNewCourses(mapped);
      setLoading(false);
    })
    .catch((err)=>{
      setError(err.message);
      setLoading(false);
    });
  },[]);

  useEffect(()=>{
    if (newCourses.length>0){
      console.log('Courses updated');
    } 
  },[newCourses]) 
  //only when newCOurses array change is the useeffect done 
const filteredCourses=merged.filter(course=>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  )

const noOfEnrolled=enrolledCourses.length;

  return (
    <div style={appLayout}>
      <Header siteName="Student Portal" enrolled={noOfEnrolled} />
      
      <main style={mainContent}>
        <h2>My Enrolled Courses</h2>
        <input type='text' value={searchTerm} placeholder='search'
        onChange={(e)=>setSerchTerm(e.target.value)}/>
        { loading
          ?
          <h3>Loading....</h3>
          :
          error
          ?
          <>
          <h2>There is an error in fetching the courses</h2>
          </>
          :
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
        }
        <StudentProfile/>
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
  alignContent:'center',
  justifyItems:'center',
};

const cardGrid = {
  display: 'flex',
  flexWrap: 'wrap',
  gap: '15px',
  marginTop: '15px',
};

export default App;