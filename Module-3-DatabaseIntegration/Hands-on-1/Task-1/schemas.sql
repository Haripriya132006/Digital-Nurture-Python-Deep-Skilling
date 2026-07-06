create database college_db;
use college_db;

create table departments(
	department_id int primary key auto_increment,
          dept_name varchar(100) not null,
          hod_name varchar(100) ,
          budget decimal(12,2)
);

create table students(
	student_id int primary key auto_increment,
          first_name varchar(50) not null,
          last_name varchar(50) not null,
          email varchar(100) unique not null,
          date_of_birth date,
          department_id int ,
          enrollment_year int,
          foreign key(department_id) references departments(department_id)
);

create table courses(
	course_id int primary key auto_increment,
          course_name varchar(150) not null,
          course_code varchar(20) unique,
          credits int,
          department_id int ,
          foreign key (department_id) references departments(department_id)
);

create table enrollments(
	enrollment_id int primary key auto_increment,
          student_id int ,
          course_id int,
          enrollment_date date,
          grade char(2) ,
          foreign key(student_id) references students(student_id) ,
          foreign key (course_id) references courses(course_id)
);

create table professors(
	professor_id int primary key auto_increment,
          prof_name varchar(100) not null,
          email varchar(100) unique,
          department_id int,
          salary decimal(10,2) ,
          foreign key(department_id) references departments(department_id)
);