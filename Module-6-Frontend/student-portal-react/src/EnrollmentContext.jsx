import {createContext,useState} from 'react';

export const EnrollmentContext=createContext();

export const EnrollmentProvider=({children})=>{
          const [enrolledCourses,setEnrolledCourses]=useState([]);

          const enrollCourse=(course)=>{
                    if(!enrolledCourses.find(c=>c.id==course.id)){
                              setEnrolledCourses([...enrolledCourses,course]);
                    }
          };
          const removeCourse=(courseId)=>{
                    setEnrolledCourses(enrolledCourses.filter(course=>course.id !== courseId));
          };

          return (
                    <EnrollmentContext.Provider value={{enrolledCourses,enrollCourse,removeCourse}}>
                              {children}
                    </EnrollmentContext.Provider>
          )
}