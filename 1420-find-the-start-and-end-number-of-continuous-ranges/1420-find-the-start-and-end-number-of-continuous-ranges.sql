# Write your MySQL query statement below

-- with CTE AS
-- (
--     SELECT 
--         log_id,
--         log_id - ROW_NUMBER() OVER(ORDER BY log_id) as group_id
--     FROM Logs
-- )

-- SELECT 
--     MIN(LOG_ID) AS start_id , 
--     MAX(log_id) AS end_id
-- FROM CTE
-- GROUP BY group_id


# Gaps and Island Solution
WITH CTE AS
(
SELECT log_id, SUM(start_signal) OVER(ORDER BY log_id) AS group_id FROM 
(
SELECT
    *,
    IF(LAG(log_id) OVER(ORDER BY log_Id) IS NULL OR LAG(log_id) OVER(ORDER BY log_Id) != log_id-1,1,0) AS start_signal
FROM Logs
) a
)

SELECT 
    MIN(LOG_ID) AS start_id , 
    MAX(log_id) AS end_id
FROM CTE
GROUP BY group_id
