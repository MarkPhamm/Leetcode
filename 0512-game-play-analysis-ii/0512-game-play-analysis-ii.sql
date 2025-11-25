# Write your MySQL query statement below
with cte as (
    select 
    player_id,
    device_id,
    dense_rank () over (partition by player_id order by event_date) as rnk
    from Activity
) 
select
    player_id,
    device_id
from cte 
where rnk = 1