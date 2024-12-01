# Write your MySQL query statement below
SELECT abs(
(SELECT MAX(salary) max_salary FROM Salaries
WHERE department = 'Engineering'
GROUP BY department) 
-
(SELECT MAX(salary) max_salary FROM Salaries
WHERE department = 'Marketing'
GROUP BY department) 
) salary_difference