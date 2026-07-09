-- use college_db;
-- desc students;
-- desc departments;

select concat(s.first_name,' ', s.last_name) full_name,d.dept_name 
from students s join departments d
on s.department_id=d.department_id;

select concat(s.first_name,' ', s.last_name) full_name  ,
c.course_name ,e.enrollment_date
from students s join enrollments e
on s.student_id=e.student_id
join courses c 
on c.course_id=e.course_id;

select concat(s.first_name,' ',s.last_name) full_name
from students s left join enrollments e
on s.student_id=e.student_id
where enrollment_id is null;

select c.course_name,count(enrollment_id) no_of_students_enrolled
from courses c left join enrollments e
on c.course_id=e.course_id
group by course_name;

-- show tables;
-- desc professors;

select d.dept_name,
ifnull(prof_name,'no proffessor yet') 'professor',
ifnull(p.salary,0) 'salary'
from departments d left join professors p 
on d.department_id=p.department_id ;