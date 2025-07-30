-- University Admission Process Database Schema

CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    address VARCHAR(500),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    gender VARCHAR(20)
);

CREATE TABLE Department (
    department_code VARCHAR(20) PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255)
);

CREATE TABLE Course (
    course_code VARCHAR(20) PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    credits INT NOT NULL,
    department_code VARCHAR(20),
    CONSTRAINT fk_course_department FOREIGN KEY (department_code) REFERENCES Department(department_code)
);

CREATE TABLE Faculty (
    faculty_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department_code VARCHAR(20),
    email VARCHAR(255),
    CONSTRAINT fk_faculty_department FOREIGN KEY (department_code) REFERENCES Department(department_code)
);

-- Junction table to handle many-to-many relationship between Faculty and Course
CREATE TABLE FacultyCourse (
    faculty_id INT,
    course_code VARCHAR(20),
    PRIMARY KEY (faculty_id, course_code),
    CONSTRAINT fk_faculty_course_faculty FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id),
    CONSTRAINT fk_faculty_course_course FOREIGN KEY (course_code) REFERENCES Course(course_code)
);

CREATE TABLE Admission (
    admission_id INT PRIMARY KEY,
    student_id INT,
    course_code VARCHAR(20),
    date DATE,
    status VARCHAR(50),
    CONSTRAINT fk_admission_student FOREIGN KEY (student_id) REFERENCES Student(student_id),
    CONSTRAINT fk_admission_course FOREIGN KEY (course_code) REFERENCES Course(course_code)
);

CREATE TABLE Exam (
    exam_id INT PRIMARY KEY,
    course_code VARCHAR(20),
    exam_date DATE,
    exam_type VARCHAR(50),
    CONSTRAINT fk_exam_course FOREIGN KEY (course_code) REFERENCES Course(course_code)
);

CREATE TABLE Result (
    result_id INT PRIMARY KEY,
    student_id INT,
    exam_id INT,
    score FLOAT,
    CONSTRAINT fk_result_student FOREIGN KEY (student_id) REFERENCES Student(student_id),
    CONSTRAINT fk_result_exam FOREIGN KEY (exam_id) REFERENCES Exam(exam_id)
);

CREATE TABLE Payment (
    payment_id INT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(10, 2),
    date DATE,
    method VARCHAR(100),
    status VARCHAR(50),
    CONSTRAINT fk_payment_student FOREIGN KEY (student_id) REFERENCES Student(student_id)
);
