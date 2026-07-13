use college_db;

select s.first_name ,count(e.enrollment_id) count 
from students s left join enrollments e
on s.student_id=e.student_id
group by s.student_id
having count(e.enrollment_id) > 
(select avg(e_count)
from (select count(e1.enrollment_id) as e_count
		from enrollments e1
		right join students s1
		on s1.student_id=e1.student_id
		group by s1.student_id) tab

);

select c.course_id, c.course_name
from Courses c
where not exists (
    select 1 
    from Enrollments e
    where e.course_id = c.course_id 
    and e.grade != 'A' or e.grade is null           
);


select p.prof_name,d.dept_name,p.salary
from professors p
join departments d on
p.department_id=d.department_id
where p.salary=(
	select max(p1.salary)
	from professors p1
	where p1.department_id=p.department_id
);

select d1.dept_name,d.avg_salary
from(
	select department_id,avg(salary) as avg_salary
    from professors
    group by department_id
) as d
join departments d1 
on d.department_id=d1.department_id
where d.avg_salary > 85000;