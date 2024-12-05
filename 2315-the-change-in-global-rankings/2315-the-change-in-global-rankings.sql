# Write your MySQL query statement below
SELECT 
    team_id, 
    name,
    CAST(DENSE_RANK() OVER (ORDER BY points DESC, name) AS SIGNED) -
    CAST(DENSE_RANK() OVER (ORDER BY (points + points_change) DESC, name) AS SIGNED)
    AS rank_diff
FROM TeamPoints
JOIN PointsChange USING(team_id)
ORDER BY 1
