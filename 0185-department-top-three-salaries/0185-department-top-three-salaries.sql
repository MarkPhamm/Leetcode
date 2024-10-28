# Write your MySQL query statement below
with cte as
(
select d.name as Department, e.name as Employee, salary as Salary, 
dense_rank() over(partition by d.name order by salary desc) ranking
from Employee e
join Department d
on e.departmentID = d.id
)
select Department, Employee, Salary from cte where ranking <= 3
order by department ,3 desc