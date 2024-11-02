# Write your MySQL query statement below

SELECT ROUND(AVG(daily_percent)*100,2) as average_daily_percent
FROM 
(
SELECT 
    action_date,
    COUNT(DISTINCT Removals.post_id)/
    COUNT(DISTINCT Actions.post_id) as daily_percent
FROM Actions
LEFT JOIN Removals
USING(post_id)
WHERE extra = 'spam'
GROUP BY 1
) a