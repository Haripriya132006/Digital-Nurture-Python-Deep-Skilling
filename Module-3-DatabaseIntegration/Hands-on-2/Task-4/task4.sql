-- use college_db;
-- desc departments;

select c.course_name, count(e.enrollment_id) total_no_of_enrollments
from courses c left join enrollments e
on c.course_id=e.course_id
group by course_name;

-- show tables;

select d.dept_name , round(avg(ifnull(p.salary,0)),2) average_salary
from departments d left join professors p
on d.department_id=p.department_id
group by dept_name;

-- desc departments;

select dept_name from departments 
group by dept_name
having sum(budget)>600000;

select g.grade, COUNT(e.grade) count
from (
    select 'A' grade union all
    select 'B' union all
    select 'C' union all
    select 'D' union all
    select 'F'
) g
left join enrollments e 
    on e.grade = g.grade
    and e.course_id = (select course_id
						from courses 
                        where course_code = 'CS101')
group by g.grade
order by grade;

-- desc courses;

-- desc enrollments;

select d.dept_name, count(d.department_id) enrolled_students
from departments d join courses c 
on c.department_id = d.department_id
join enrollments e
on e.course_id = c.course_id
group by d.department_id
having enrolled_students >2
