# Write your MySQL query statement below

SELECT 
    gender,
    day,
    SUM(score_points) OVER(partition by gender ORDER BY day) total
FROM Scores
ORDER BY 1,2