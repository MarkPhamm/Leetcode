-- # Write your MySQL query statement below

-- SELECT distinct id, name FROM Students
-- WHERE department_id NOT IN (SELECT distinct id FROM Departments)
SELECT s.id, s.name FROM students s
LEFT JOIN departments d ON d.id = department_id
WHERE d.id IS NULL;