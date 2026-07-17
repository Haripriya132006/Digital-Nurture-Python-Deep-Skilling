// pages/CoursesPage.jsx
import { useState, useEffect } from 'react';
import CourseCard from '../components/CourseCard';
import { useNavigate } from 'react-router-dom';

// import { useContext } from 'react';
// import { EnrollmentContext } from '../EnrollmentContext';

import { useSelector,useDispatch } from 'react-redux';
import {enroll} from '../store/enrollmentSlice';

function CoursesPage() {
  const enrolledCourses =useSelector((state)=>state.enrollment.enrolledCourses);
  const dispatch=useDispatch();
  const navigate = useNavigate();
  const courses = [
    { id: 1, name: "Python", code: "IT101", credits: 3, grade: "A" },
    { id: 2, name: "System Design", code: "CS101", credits: 4, grade: "A" },
    { id: 3, name: "Web Designing", code: "IT201", credits: 5, grade: "A" },
    { id: 4, name: "Database Management System", code: "CS201", credits: 3, grade: "A" },
    { id: 5, name: "Spring Boot", code: "IT301", credits: 4, grade: "A" },
  ];

  const [searchTerm, setSearchTerm] = useState('');
  const [newCourses, setNewCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const merged = [...courses, ...newCourses];

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then((response) => {
        if (!response.ok) throw new Error('Failed to fetch courses data.');
        return response.json();
      })
      .then((data) => {
        const mapped = data.slice(0, 5).map((post) => ({
          id: post.id + courses.length,
          name: post.title,
          code: `CS${post.id + 400}`,
          credits: post.id % 2 === 0 ? 4 : 3,
          grade: 'Pending',
        }));
        setNewCourses(mapped);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const filteredCourses = merged.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <h2>Available Courses</h2>
      <button onClick={()=>navigate('/profile')}> student profile</button>
      <input
        type="text"
        value={searchTerm}
        placeholder="Search courses..."
        onChange={(e) => setSearchTerm(e.target.value)}
        style={{ padding: '8px', marginBottom: '15px', width: '100%', maxWidth: '300px' }}
      />

      {loading ? (
        <h3>Loading....</h3>
      ) : error ? (
        <h2>There is an error in fetching the courses: {error}</h2>
      ) : (
        <div style={cardGrid}>
          {filteredCourses.map((course) => (
            <div key={course.id} style={{ cursor: 'pointer' }}>
              <CourseCard
                name={course.name}
                code={course.code}
                credits={course.credits}
                grade={course.grade}
                onEnroll={() => dispatch(enroll(course))}
                isEnrolled={enrolledCourses.some(c=>c.id===course.id)}
              />
              {/* Clicking this wrapper or a "View Details" button can navigate to dynamic route */}
              <button 
                onClick={() => navigate(`/courses/${course.id}`)}
                style={{ marginTop: '5px', padding: '5px 10px', fontSize: '0.8rem' }}
              >
                View Details
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

const cardGrid = {
  display: 'flex',
  flexWrap: 'wrap',
  gap: '15px',
  marginTop: '15px',
};

export default CoursesPage;