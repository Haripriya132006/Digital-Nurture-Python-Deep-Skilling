// import React from 'react';
// import { useContext } from 'react';
// import { EnrollmentContext } from '../EnrollmentContext';
import { useNavigate } from 'react-router-dom';

import {useSelector,useDispatch} from 'react-redux';
import {unenroll} from '../store/enrollmentSlice';


function ProfilePage() {
  // const{enrolledCourses,removeCourse}=useContext(EnrollmentContext);
  const navigate=useNavigate();

  const dispatch=useDispatch();
  const enrolledCourses=useSelector((state)=>state.enrollment.enrolledCourses);
  return (
    <div>
      <h2>Your Profile</h2>
      <h3>Enrolled Courses</h3>

      <button onClick={()=>navigate('/courses')}>courses</button>
      {enrolledCourses.length === 0 ? (
        <p>You haven't enrolled in any courses yet.</p>
      ) : (
        <ul>
          {enrolledCourses.map(course => (
            <li key={course.id}>
              {course.name} 
              <button onClick={() => dispatch(unenroll(course.id))} style={{ marginLeft: '10px', color: 'red' }}>Un-enroll</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProfilePage;