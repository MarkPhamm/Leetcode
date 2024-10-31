# Write your MySQL query statement below

SELECT dept_name, COUNT(student_id) as student_number FROM Department
LEFT JOIN Student
USING(dept_id)
GROUP BY 1
ORDER BY 2 DESC