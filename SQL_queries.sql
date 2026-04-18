1. Create Database
CREATE DATABASE hospital_db;
USE hospital_db;

2. Create Table
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(50),
    doctor VARCHAR(50),
    treatment_cost INT
);

3. Insert Data
INSERT INTO patients VALUES
(1,45,'Male','Diabetes','Dr Shah',5000),
(2,30,'Female','Fever','Dr Patil',2000),
(3,55,'Male','Heart Disease','Dr Shah',20000),
(4,22,'Female','Flu','Dr Kulkarni',1500),
(5,40,'Male','Diabetes','Dr Shah',4500);

4. Display Patient Records
SELECT * FROM patients;

5. Count Patients by Disease
SELECT disease, COUNT(*) AS patient_count
FROM patients
GROUP BY disease;

6. Average Treatment Cost
SELECT AVG(treatment_cost) AS avg_cost
FROM patients;

7. Doctor Treating Most Patients
SELECT doctor, COUNT(*) AS total_patients
FROM patients
GROUP BY doctor
ORDER BY total_patients DESC
LIMIT 1;