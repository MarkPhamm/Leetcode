-- Write your MySQL query statement below

WITH 
    distinct_logins AS (
        -- Step 1: Get distinct login records
        SELECT DISTINCT id, login_date
        FROM Logins
    ),
    
    login_lags AS (
        -- Step 2: Compute the previous login date and the signal ID
        SELECT 
            a.id,
            a.login_date,
            LAG(a.login_date) OVER (PARTITION BY a.id ORDER BY a.login_date) AS prev_login,
            CASE
                WHEN LAG(a.login_date) OVER (PARTITION BY a.id ORDER BY a.login_date) IS NULL
                     OR LAG(a.login_date) OVER (PARTITION BY a.id ORDER BY a.login_date) + INTERVAL 1 DAY < a.login_date
                THEN 1
                ELSE 0
            END AS signal_id
        FROM distinct_logins a
    ),
    
    grouped_logins AS (
        -- Step 3: Create group_id based on the signal_id
        SELECT
            id,
            login_date,
            signal_id,
            SUM(signal_id) OVER (PARTITION BY id ORDER BY login_date) AS group_id
        FROM login_lags
    )

-- Final result: Select users with at least 5 distinct groupings
SELECT DISTINCT 
    b.id,
    a.name
FROM 
    grouped_logins b
JOIN 
    Accounts a ON a.id = b.id
GROUP BY 
    b.id, a.name, b.group_id
HAVING 
    COUNT(b.group_id) >= 5;
