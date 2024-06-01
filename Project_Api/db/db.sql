CREATE DATABASE db_pre_tesis;
use db_pre_tesis;
ALTER DATABASE db_pre_tesis CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE user_type (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10)
);

CREATE TABLE role (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10)
);

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(80) NOT NULL,
    avatar VARCHAR(255) DEFAULT(NULL),
    password VARCHAR(255) NOT NULL,
    status ENUM('ACTIVE', 'INACTIVE', 'SUSPENDED') DEFAULT 'ACTIVE',
    user_type_id INT,
    role_id INT,
    FOREIGN KEY (user_type_id) REFERENCES user_type(id),
    FOREIGN KEY (role_id) REFERENCES role(id)
);

CREATE TABLE career (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE section (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    cycle INT,
    career_id INT,
    FOREIGN KEY (career_id) REFERENCES career(id)
);

CREATE TABLE course (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    career_id INT,
    FOREIGN KEY (career_id) REFERENCES career(id)
);

CREATE TABLE student (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    paternal_surname VARCHAR(255),
    maternal_surname VARCHAR(255),
    section_id INT,
    user_id INT UNIQUE,
    FOREIGN KEY (section_id) REFERENCES section(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE teacher (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    paternal_surname VARCHAR(255),
    maternal_surname VARCHAR(255),
    user_id INT UNIQUE,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE student_courses (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    section_id INT,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (course_id) REFERENCES course(id),
    FOREIGN KEY (section_id) REFERENCES section(id)
);

CREATE TABLE teacher_courses (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    teacher_id INT,
    course_id INT,
    section_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teacher(id),
    FOREIGN KEY (course_id) REFERENCES course(id),
    FOREIGN KEY (section_id) REFERENCES section(id)
);

CREATE TABLE attendance (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date DATETIME,
    career_id INT,
    FOREIGN KEY (career_id) REFERENCES career(id),
    section_id INT,
    FOREIGN KEY (section_id) REFERENCES section(id),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES course(id)
);

CREATE TABLE attendance_student(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    attendance_id INT,
    student_id INT,
    date DATETIME,
    status ENUM('PRESENT', 'ABSENT', 'LATE'),
    FOREIGN KEY (attendance_id) REFERENCES attendance(id),
    FOREIGN KEY (student_id) REFERENCES student(id)
);