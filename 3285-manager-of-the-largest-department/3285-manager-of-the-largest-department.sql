# Write your MySQL query statement below

WITH Counting_employee AS
(
    SELECT *, COUNT(emp_id) OVER(PARTITION BY dep_id) no_employee FROM Employees
),
Ranking_department AS
(
    SELECT *, RANK() OVER(ORDER BY no_employee DESC) ranking FROM Counting_employee
)
SELECT emp_name manager_name, dep_id FROM ranking_department
WHERE ranking = 1 and position = 'Manager'
ORDER BY 2