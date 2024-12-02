# Write your MySQL query statement below
SELECT 
    DISTINCT user_id
FROM emails
LEFT JOIN texts USING(email_id)
WHERE signup_action = "Verified"
AND DATE(signup_date) + INTERVAL 1 DAY = DATE(action_date)
ORDER BY 1