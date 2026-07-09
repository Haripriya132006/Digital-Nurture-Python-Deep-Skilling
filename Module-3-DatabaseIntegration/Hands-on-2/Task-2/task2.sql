-- desc students;

select * from students 
where enrollment_year=2022 
order by first_name,last_name;

-- desc courses;

select * from courses 
where credits>3
order by credits desc;

-- desc professors;

select * from professors
where salary between 80000 and 95000;

select * from students 
where email like "%@college.edu";


select enrollment_year ,count(*) no_of_enrollments 
from students
group by enrollment_year
order by enrollment_year;