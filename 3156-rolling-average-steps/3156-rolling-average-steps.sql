# Write your MySQL query statement below
SELECT user_id, steps_date, round(rolling_average, 2) rolling_average FROM 
(
SELECT
    *,
    AVG(steps_count) OVER(PARTITION BY user_id ORDER BY steps_date RANGE BETWEEN INTERVAL 2 DAY PRECEDING AND CURRENT ROW) rolling_average,
    COUNT(steps_date) OVER(PARTITION BY user_id ORDER BY steps_date RANGE BETWEEN INTERVAL 2 DAY PRECEDING AND CURRENT ROW) count_range  
FROM Steps
) a
WHERE count_range = 3
ORDER BY 1,2