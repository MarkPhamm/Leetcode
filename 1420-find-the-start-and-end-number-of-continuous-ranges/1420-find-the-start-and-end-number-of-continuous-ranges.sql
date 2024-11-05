# Write your MySQL query statement below

with CTE AS
(
    SELECT 
        log_id,
        log_id - ROW_NUMBER() OVER(ORDER BY log_id) as group_id
    FROM Logs
)

SELECT 
    MIN(LOG_ID) AS start_id , 
    MAX(log_id) AS end_id
FROM CTE
GROUP BY group_id
