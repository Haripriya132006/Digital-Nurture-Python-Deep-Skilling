alter table students 
add column phone_number VARCHAR(15);

alter table courses 
add column max_seats INT DEFAULT 60;

alter table enrollments 
add constraint chk_grade CHECK (grade IN ('A', 'B', 'C', 'D', 'F'));

alter table departments 
change column hod_name head_of_dept VARCHAR(100);

alter table students 
drop column phone_number;
