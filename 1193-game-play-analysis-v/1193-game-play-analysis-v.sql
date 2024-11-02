# Write your MySQL query statement below
WITH cte as
(
SELECT 
    player_id, 
    event_date,
    lead(event_date) over(partition by player_id order by event_date) as next_login,
    rank() over(partition by player_id order by event_date) as ranking
FROM Activity
)


SELECT 
    event_date AS install_dt, 
    count(DISTINCT player_id) AS installs, 
    round((COUNT(DISTINCT IF(event_date + INTERVAL 1 DAY = next_login, player_id, null))+0.0)/count(DISTINCT player_id),2) AS Day1_retention
FROM cte
WHERE ranking = 1
GROUP BY 1