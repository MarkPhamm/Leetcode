# Write your MySQL query statement below
SELECT emp_id, firstname, lastname, MAX(salary) salary, department_id FROM Salary
GROUP BY  emp_id, firstname, lastname,department_id
ORDER BY emp_id