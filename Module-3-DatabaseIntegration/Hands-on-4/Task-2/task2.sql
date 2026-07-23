create index idx_student_enrollment_year 
on students(enrollment_year);

create unique index idx_unique_student_course
on enrollments(student_id,course_id);

create index idx_course_code
on courses(course_code);

explain format=json
select s.first_name,s.lanst_name,c.course_name
from enrollments e join students s 
on s.student_id = e.student_id
join courses c
on c.course_id=e.course_id
where s.enrollment_year=2022;