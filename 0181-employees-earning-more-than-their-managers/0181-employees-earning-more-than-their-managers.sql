# Write your MySQL query statement below
SELECT a.name as "Employee" from Employee a 
JOIN Employee b
ON b.id = a.managerId
WHERE a.salary > b.salary


#b.name as "Employee", a.name as "Manager"