# Write your MySQL query statement below
select * from Users
where email REGEXP '^[A-Za-z0-9]+@[A-Za-z]+\\.com$'
order by 1