# Write your MySQL query statement below
with cte as
(
select player_id, datediff( 
lead(event_date) over(partition by player_id order by event_date),event_date) diff,
rank() over(partition by player_id order by event_date) ranking
from Activity
)
select round(count(distinct(player_id))
/
(
  SELECT count(distinct(player_id)) from Activity
),2) as fraction 
from cte
where diff = 1 and ranking = 1