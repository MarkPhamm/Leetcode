# Write your MySQL query statement below
WITH CTE as
(
SELECT 
*, 
LEAD(student) over(order by id) as shift_forward,
LAG(student) over(order by id) as shift_backward

FROM Seat
)
SELECT id, 
CASE 
WHEN shift_forward is null and id%2=1 then Student
WHEN id%2=1 then shift_forward
WHEN id%2=0 then shift_backward
END AS student

FROM CTE