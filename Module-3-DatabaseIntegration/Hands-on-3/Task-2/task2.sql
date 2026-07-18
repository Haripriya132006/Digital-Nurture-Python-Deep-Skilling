drop view vw_student_enrollment_summary;

create view vw_student_enrollment_summary as
select concat(s.first_name,' ', s.last_name) full_name,
          d.dept_name,
          count(e.course_id) as number_of_courses_enrolled_in,
          avg(case
                    when e.grade='A' then 4
                    when e.grade='B' then 3
                    when e.grade='C' then 2
                    when e.grade='D' then 1
                    when e.grade='F' then 0
                    else 0
                    end
          ) as gpa
from students s left join enrollments e 
on s.student_id=e.student_id
join departments d
on s.department_id=d.department_id
group by s.student_id,s.first_name,s.last_name,d.dept_name;


create view vw_course_stats as
select c.course_name,c.course_code,
	count(e.student_id) as total_enrollments,
	avg(case
		when e.grade='A' then 4
                    when e.grade='B' then 3
                    when e.grade='C' then 2
                    when e.grade='D' then 1
                    when e.grade='F' then 0
                    else null
                    end
          ) as avg_gpa
from courses c left join enrollments e 
on c.course_id=e.course_id
group by c.course_id,c.course_name,c.course_code;

select * from vw_student_enrollment_summary;

select full_name,gpa
from vw_student_enrollment_summary
where gpa>3.0;

update vw_student_enrollment_summary
set dept_name='Mechanical' 
where full_name='Harry K';

drop view vw_student_enrollment_summary;
drop view vw_course_stats;

create view vw_student_enrollment_summary as
select student_id,first_name,last_name,department_id
from students
where department_id=1
with check option

