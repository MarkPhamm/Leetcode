# Write your MySQL query statement below
WITH cte AS
(
    SELECT 
        user_id,
        activity_date,
        RANK() OVER(PARTITION BY user_id ORDER BY activity_date) ranking
    FROM Traffic
    WHERE activity = 'login' 
)
SELECT 
    activity_date as login_date,
    COUNT(DISTINCT user_id) as user_count
FROM cte
WHERE ranking = 1 AND
(Activity_date BETWEEN "2019-06-30" - INTERVAL 90 DAY AND "2019-06-30" )
OR (Activity_date BETWEEN "2019-06-30" AND "2019-06-30" + INTERVAL 90 DAY)
GROUP BY 1
