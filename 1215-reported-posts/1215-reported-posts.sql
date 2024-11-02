# Write your MySQL query statement below
SELECT 
    extra as report_reason,
    COUNT(Distinct post_id) as report_count
FROM Actions
WHERE action = 'report'
AND action_date = "2019-07-05" - INTERVAL 1 DAY
GROUP BY 1