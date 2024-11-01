# Write your MySQL query statement below
SELECT project_id, employee_Id FROM 
(
SELECT 
    Project.project_id, 
    employee_Id,
    RANK() OVER(Partition BY Project.Project_id ORDER BY experience_years DESC) ranking 
FROM Project
JOIN Employee
USING(employee_id)
) a
WHERE ranking = 1