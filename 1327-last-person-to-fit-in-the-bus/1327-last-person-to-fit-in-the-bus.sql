# Write your MySQL query statement below
with cte as
(
select *,
sum(weight) over(order by turn) as running_total
from queue
)
select person_name from cte
where running_total <=1000
order by turn desc
limit 1