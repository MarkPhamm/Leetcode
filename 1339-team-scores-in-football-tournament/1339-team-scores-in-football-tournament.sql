# Write your MySQL query statement below

with points as
(
SELECT 
    host_team,
    guest_team,
    CASE 
        WHEN host_goals > guest_goals THEN 3
        WHEN host_goals < guest_goals THEN 0
        ELSE 1
    END AS host_point,
    CASE 
        WHEN guest_goals > host_goals THEN 3
        WHEN guest_goals < host_goals THEN 0
        ELSE 1
    END AS guest_point
FROM matches
)

SELECT Teams.team_id,team_name, IFNULL(SUM(goal),0) AS num_points FROM 
(
SELECT 
    host_team as team_id,
    host_point as goal
FROM points
UNION ALL
SELECT 
    guest_team as team_id,
    guest_point as goal
FROM points
) a
RIGHT JOIN Teams
USING(team_id)
GROUP BY 1,2
ORDER BY 3 DESC, 1