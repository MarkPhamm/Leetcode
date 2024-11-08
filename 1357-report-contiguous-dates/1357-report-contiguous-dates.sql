-- # Write your MySQL query statement below

WITH all_period AS (
    SELECT
        fail_date AS date,
        'failed' AS period_state
    FROM failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    
    UNION
    
    SELECT
        success_date AS date,
        'succeeded' AS period_state
    FROM succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
),

start_signals AS (
    SELECT 
        *,
        CASE 
            WHEN LAG(period_state) OVER (ORDER BY date) != period_state 
                 OR LAG(period_state) OVER (ORDER BY date) IS NULL 
            THEN 1 
            ELSE 0 
        END AS start_signal
    FROM all_period
),

group_ids AS (
    SELECT 
        date,
        period_state, 
        SUM(start_signal) OVER (ORDER BY date) AS group_id
    FROM start_signals
)

SELECT
    period_state, 
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM group_ids
GROUP BY group_id, period_state
ORDER BY start_date;



    