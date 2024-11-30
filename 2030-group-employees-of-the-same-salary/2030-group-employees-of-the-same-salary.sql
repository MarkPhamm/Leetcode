# Write your MySQL query statement below
WITH number_of_members AS
(
SELECT 
    *, 
    COUNT(employee_id) OVER(PARTITION BY salary) number_of_member 
FROM Employees
)

SELECT 
    employee_id,
    name,
    salary,
    DENSE_RANK() OVER(ORDER BY salary) team_id 
FROM number_of_members
WHERE number_of_member != 1
ORDER BY team_id, employee_id