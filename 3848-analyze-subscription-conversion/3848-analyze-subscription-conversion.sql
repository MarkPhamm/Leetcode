# Write your MySQL query statement below

SELECT 
    user_id, 
    ROUND(AVG(IF(activity_type = 'free_trial', activity_duration, null)),2) trial_avg_duration,
    ROUND(AVG(IF(activity_type = 'paid', activity_duration, null)),2) paid_avg_duration
FROM UserActivity
GROUP BY 1
HAVING ROUND(AVG(IF(activity_type = 'paid', activity_duration, null)),2) > 0
ORDER BY 1