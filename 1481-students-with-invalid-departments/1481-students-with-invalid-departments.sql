# Write your MySQL query statement below

SELECT distinct id, name FROM Students
WHERE department_id NOT IN (SELECT distinct id FROM Departments)