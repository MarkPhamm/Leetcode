-- Write your MySQL query statement below
WITH CTE AS (
    SELECT 
        age_bucket, 
        activity_type, 
        SUM(time_spent) AS total_time
    FROM Activities
    JOIN Age USING (user_id)
    GROUP BY age_bucket, activity_type
    ORDER BY age_bucket, activity_type
), 
open_cte AS (
    SELECT * FROM CTE WHERE activity_type = 'open'
), 
send_cte AS (
    SELECT * FROM CTE WHERE activity_type = 'send'
) 
SELECT 
    age_bucket, 
    ROUND(send_cte.total_time / (send_cte.total_time + IFNULL(open_cte.total_time,0)) * 100, 2) AS send_perc,
    ROUND(IFNULL(open_cte.total_time,0) / (send_cte.total_time + IFNULL(open_cte.total_time,0)) * 100, 2) AS open_perc
FROM send_cte
LEFT JOIN open_cte USING (age_bucket);
