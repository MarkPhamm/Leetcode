# Write your MySQL query statement below
with cte as (
    select
        x, 
        lag(x,1) over(order by x) as px
    from Point
)

select min(abs(x-px)) as shortest from cte