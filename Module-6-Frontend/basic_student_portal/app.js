import  {courses} from "./data.js";

console.log("Courses: ");
courses.forEach(course => {
      const {name,credits} = course;
      console.log('Name:',name,'- Credits',credits);
})
const formattedCourse=courses.map(course=>{
      return (course.code+' - ' + course.name+' - '+course.credits); 
})
console.log("formatted ",formattedCourse);

const highcredit=courses.filter(course=>course.credits>=4);
console.log("courses with high credits",highcredit.length);

const totcred=courses.reduce((accumulator,course)=>{
      return accumulator+course.credits;
},0);

console.log("total credits",totcred);

export const courseGrid=document.querySelector('.course-grid'); 
export default function renderCourses(courses){
      courseGrid.innerHTML='';
      courses.forEach(course => {
            const article = document.createElement('article');
            article.className='course-card';
            article.innerHTML=`
            <h3>${course.name}</h3>
            <p>Code:${course.code}</p>
            <span>Credits:${course.credits}</span>
            `;
            courseGrid.appendChild(article);
});
}
// renderCourses(courses)
const totalCreditsValue=courses.reduce((sum,course)=> sum+course.credits,0);
const totalCreditsParagraph=document.getElementById('total-credits');

totalCreditsParagraph.textContent=`Total Enrolled Credits: ${totalCreditsValue}`;

const searchInput = document.getElementById('search-courses');
const sortButton = document.getElementById('sort-credits');

searchInput.addEventListener('input', (event) => {
      const query = event.target.value.toLowerCase();

// Filter by name (case-insensitive conversion)
      const filtered = courses.filter(course => 
      course.name.toLowerCase().includes(query)
      );
      
      renderCourses(filtered);
});

sortButton.addEventListener('click', () => {
    // Slice a shallow copy first so we don't accidentally scramble the master data order permanently
      const sorted = [...courses].sort((a, b) => b.credits - a.credits);
      renderCourses(sorted);
});