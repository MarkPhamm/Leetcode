# Write your MySQL query statement below

SELECT distinct user_id
FROM 
(
SELECT
    user_id, 
    TIMESTAMPDIFF(day, lag(created_at) OVER(PARTITION BY user_id ORDER BY created_at), created_at) diff
FROM users
) a
WHERE diff <= 7 AND diff IS NOT NULL
ORDER BY 1