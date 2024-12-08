# Write your MySQL query statement below

SELECT 
    student_id, 
    department_id, 
    IFNULL(ROUND((RANK() OVER(PARTITION BY department_id ORDER BY mark DESC)-1)/
    (COUNT(mark) OVER(PARTITION BY department_id)-1)*100,2),0) percentage
FROM Students 