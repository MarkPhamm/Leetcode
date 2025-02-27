# Write your MySQL query statement below

SELECT FLOOR(SUM(hour_diff/60)/24) total_uptime_days FROM 
(
SELECT 
    *, 
    LAG(status_time) OVER (PARTITION BY server_id ORDER BY status_time) AS prev,
    TIMESTAMPDIFF(minute, LAG(status_time) OVER (PARTITION BY server_id ORDER BY status_time), status_time) AS hour_diff 
FROM Servers
) a
WHERE session_status = 'stop'