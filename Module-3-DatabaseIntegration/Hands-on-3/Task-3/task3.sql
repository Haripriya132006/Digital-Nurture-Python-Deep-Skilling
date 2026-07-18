delimiter //
create procedure sp_enroll_student(
	in p_student_id int,
    in p_course_id int,
    in p_enrollment_date date
)
begin 
	declare v_exists int default 0;
    select count(*) into v_exists
    from enrollments
    where student_id=p_student_id and course_id=p_course_id;
    
    if v_exists>0 then
		signal sqlstate '45000'
        set message_text='Duplicate enrollment found';
	else
		insert into enrollments(student_id,course_id,enrollment_date)
        values (p_student_id,p_course_id,p_enrollment_date);
	end if;
end 
//delimiter ;
   
create table department_transfer_log(
log_id int auto_increment primary key,
student_id int,
old_department_id int,
new_department_id int,
transfer_date timestamp default current_timestamp
);

delimiter //
create procedure sp_transfer_student(
	in p_student_id int,
    in p_new_dept_id int
)
begin 
	declare v_old_dept_id int;
    
    declare exit handler for sqlexception
    begin 
		rollback;
        resignal;
	end;
    
    select department_id into v_old_dept_id
    from students
    where student_id=p_student_id;
    
    start transaction;
    
    update students 
    set department_id=p_new_dept_id
    where student_id=p_student_id;
    
    insert into department_transfer_log
    (student_id,old_department_id,new_department_id)
    values (p_student_id,v_old_dept_id,p_new_dept_id);
	
    commit;
end 
// delimiter ;

CALL sp_transfer_student(1, 10); 
-- 1 is student id  
-- 10 is transfer_department_id

select * from enrollments;
start transaction;
	insert into enrollments(student_id,course_id,enrollment_date)
    values (1,5,curdate());
    
    savepoint first_insert;
    
	insert into enrollments(student_id,course_id,enrollment_date)
    values (1,5,curdate());
    
    rollback to savepoint first_insert;
commit;

    

    