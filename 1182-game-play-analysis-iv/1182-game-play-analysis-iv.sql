-- Write your MySQL query statement below
WITH cte AS (
    SELECT
        player_id,
        DATEDIFF(
            LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date),
            event_date
        ) AS diff,
        RANK() OVER (PARTITION BY player_id ORDER BY event_date) AS ranking
    FROM Activity
)

SELECT
    ROUND(
        COUNT(DISTINCT player_id) /
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM cte
WHERE diff = 1
  AND ranking = 1;
