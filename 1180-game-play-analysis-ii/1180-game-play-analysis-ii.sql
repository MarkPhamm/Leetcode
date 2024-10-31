# Write your MySQL query statement below
SELECT player_id, device_id FROM
(
SELECT 
    player_id, 
    device_id, 
    RANK() OVER(PARTITION BY player_id ORDER BY event_date) ranking 
FROM Activity
) a
WHERE ranking = 1