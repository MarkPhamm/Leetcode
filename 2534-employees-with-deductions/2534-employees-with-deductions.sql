# Write your MySQL query statement below
WITH cte AS
(
    SELECT 
        employee_id, 
        SUM(ROUND(timestampdiff(second, in_time, out_time)/60)) worked 
    FROM Logs
    GROUP BY 1
)
SELECT  employee_id FROM Employees
LEFT JOIN Cte USING(employee_id)
WHERE needed_hours * 60 > ifnull(worked,0)