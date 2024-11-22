# Write your MySQL query statement below
SELECT distinct user_id FROM 
(
SELECT 
    user_id, 
    time_stamp, 
    TIMESTAMPDIFF(SECOND, LAG(time_stamp) OVER(partition by user_id ORDER BY time_stamp), time_stamp) diff
FROM Confirmations
) a
WHERE diff <= 86400