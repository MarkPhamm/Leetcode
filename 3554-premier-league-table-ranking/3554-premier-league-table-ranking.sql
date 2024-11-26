# Write your MySQL query statement below

SELECT 
    team_id, 
    team_name,
    wins*3 + draws*1 as points,
    RANK() OVER(ORDER BY wins*3 + draws*1 DESC) position
FROM TeamStats
ORDER BY 4, 2