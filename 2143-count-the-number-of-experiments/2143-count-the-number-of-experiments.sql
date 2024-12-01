# Write your MySQL query statement below
with platforms as(
    SELECT 'IOS' AS platform UNION SELECT 'Android' UNION SELECT 'Web'
), 
experiment_names as (
    SELECT 'Programming' AS experiment_name UNION SELECT 'Sports' UNION SELECT 'Reading'
)
SELECT platform, experiment_name, COUNT(experiment_id) num_experiments FROM platforms
JOIN experiment_names
LEFT JOIN Experiments using(platform, experiment_name)
GROUP BY platform, experiment_name