# Write your MySQL query statement below


SELECT 
ifnull(ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id), 2),0.00) AS average_sessions_per_user
FROM Activity
WHERE activity_date >= ("2019-07-27" - INTERVAL 29 DAY) AND activity_date <= "2019-07-27"