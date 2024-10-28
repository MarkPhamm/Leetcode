# Write your MySQL query statement below
select IFNULL((
select distinct(salary) from
(
select *, dense_rank() over(order by salary desc) ranking from Employee
) a
where ranking = 2),null) as SecondHighestSalary
