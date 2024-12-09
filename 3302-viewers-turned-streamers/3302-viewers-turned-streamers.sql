-- Write your MySQL query statement below

WITH first_as_viewers AS (
    SELECT user_id 
    FROM (
        SELECT 
            *,
            RANK() OVER (PARTITION BY user_id ORDER BY session_start) AS rnk
        FROM Sessions
    ) a
    WHERE rnk = 1 AND session_type = 'Viewer'
)

SELECT 
    user_id, 
    COUNT(session_id) AS sessions_count 
FROM Sessions
WHERE user_id IN (SELECT user_id FROM first_as_viewers)
  AND session_type = 'Streamer'
GROUP BY user_id
ORDER BY sessions_count DESC, user_id DESC;
