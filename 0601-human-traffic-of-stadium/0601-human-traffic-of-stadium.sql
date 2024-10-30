# Write your MySQL query statement below
with cte as
(
select *,
lead(people) over(order by id) as one_after,
lead(people,2) over(order by id) as two_after,
lag(people) over(order by id) as one_before,
lag(people,2) over(order by id) as two_before
from Stadium
)
select id, visit_date, people from cte
where (people >= 100 and one_after >= 100 and two_after>=100)
or (people >= 100 and one_before>= 100 and two_before>=100)
or (people >= 100 and one_before>= 100 and one_after >=100)