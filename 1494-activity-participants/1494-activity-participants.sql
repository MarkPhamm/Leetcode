# Write your MySQL query statement below

WITH activity_count AS (
    SELECT 
        activity,
        COUNT(distinct id) AS count
    FROM Friends
    GROUP BY 1
)
SELECT activity FROM
(
SELECT 
    *,
    RANK() OVER(ORDER BY count) AS ranking_asc,
    RANK() OVER(ORDER BY count DESC) AS ranking_desc
FROM activity_count
) a
WHERE ranking_asc != 1 AND ranking_desc != 1