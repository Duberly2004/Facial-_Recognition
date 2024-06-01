INSERT INTO user_type (id,name) VALUES 
(1,'Admin'), 
(2,'User');

INSERT INTO role (id,name) VALUES 
(1,'Admin'), 
(2,'Teacher'), 
(3,'Student');

INSERT INTO user (id,email, password, user_type_id, role_id,avatar) VALUES 
(1,'duberly.mondragon@tecsup.edu.pe', 'Tecsup1234', 2, 3,'images/duberly.jpeg'), 
(2,'ethan.arredondo@tecsup.edu.pe', 'Tecsup1234', 2, 3,'images/ethan.jpeg'), 
(3,'mark@tecsup.edu.pe', 'Tecsup1234', 2, 3,'images/zuckerberg.jpg'), 
(4,'daniela@tecsup.edu.pe', 'Tecsup1234', 2, 3,'images/daniela.jpeg'),
(5,'elonkmusk@tecsup.edu.pe', 'Tecsup1234', 2, 3,'images/elon-musk.jpg'),
(6,'ana@gmail.com', 'Tecsup1234', 2, 3,'images/ana.png'),
(7,'maria@gmail.com', 'Tecsup1234', 2, 3,'images/maria.png');

INSERT INTO career (id,name) VALUES 
(1,'Diseño y desarrollo de software'), 
(2,'Procesos quimicos y metalúrgicos'), 
(3,'Big Data');

INSERT INTO section (id,name, cycle, career_id) VALUES 
(1,'C24A', 1, 1), 
(2,'C24B', 2, 1), 
(3,'C24C', 1, 1);

INSERT INTO course (id,name,career_id) VALUES 
(1,'Programación Moviles Avanzado',1), 
(2,'Desarrollo de aplicaciones Moviles Avanzado',1), 
(3,'Desarrollo de soluciones en la nube',1);

INSERT INTO student (id,name, paternal_surname, maternal_surname, section_id, user_id) VALUES 
(1,'Duberly Ivan', 'Mondragón', 'Manchay', 1, 1), 
(2,'Ethan Sebastian', 'Arredondo', 'Yarihuaman', 1, 2),
(3,'Mark', 'zuckerberg', 'Suarez', 1, 3),
(4,'Daniela', 'Cuellar', 'Vargas', 1, 4),
(5,'Elon', 'Musk', 'Arredondo', 1, 5),
(6,'Ana', 'Peréz', 'Lopez', 1, 6),
(7,'Maria', 'Porraz', 'Vega', 1, 7);

INSERT INTO teacher (id,name, paternal_surname, maternal_surname, user_id) VALUES 
(1,'Daniela', 'Smith', 'Doe', 3);

INSERT INTO student_courses (id,student_id, course_id, section_id)  VALUES 
(1,1, 1, 1), 
(2,2, 2, 2);

-- INSERT INTO attendance (id,date,career_id,section_id,course_id) VALUES
-- (1,"2020-08-12",1,1,1);

-- INSERT INTO attendance_student (id,attendance_id,student_id,date,status) VALUES
-- (1,30,1,"2020-08-12","PRESENT");