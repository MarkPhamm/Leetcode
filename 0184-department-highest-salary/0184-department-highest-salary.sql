# Write your MySQL query statement below
# Write your MySQL query statement below
Select Department, Employee, Salary from
(
   select DENSE_RANK() OVER(PARTITION BY Department.name ORDER BY Employee.salary DESC) as 
"Rank",
    Department.name as Department, Employee.name as Employee, Employee.salary as Salary from Employee 
    join Department
    on Employee.departmentID = Department.id
) as sub
where sub.Rank = 1
