# Write your MySQL query statement below
WITH cte AS
(
SELECT project_id, RANK() OVER(ORDER BY COUNT(distinct employee_id) DESC) ranking FROM Project
GROUP BY 1
)
SELECT project_id FROM cte 
WHERE ranking = 1