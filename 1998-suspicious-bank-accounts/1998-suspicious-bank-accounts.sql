-- Write your MySQL query statement below

WITH monthly_income AS (
    SELECT 
        account_id, 
        DATE_FORMAT(day, "%Y-%m") AS month, 
        SUM(amount) AS total_amount
    FROM Transactions
    WHERE type = 'creditor'
    GROUP BY account_id, month
    ORDER BY account_id, month
),
flagged_income AS (
    SELECT 
        account_id, 
        month, 
        IF(total_amount > max_income, 'Yes', 'No') AS flag
    FROM monthly_income 
    JOIN Accounts USING(account_id)
    ORDER BY account_id
),
lagged_flags AS (
    SELECT 
        account_id,
        month,
        flag,
        LAG(flag) OVER (PARTITION BY account_id ORDER BY month) AS prev_flag,
        LAG(month) OVER (PARTITION BY account_id ORDER BY month) AS prev_month
    FROM flagged_income
)
SELECT DISTINCT account_id
FROM lagged_flags
WHERE 
    flag = 'Yes'
    AND prev_flag = 'Yes'
    AND DATE_ADD(STR_TO_DATE(CONCAT(prev_month, '-01'), '%Y-%m-%d'), INTERVAL 1 MONTH) = STR_TO_DATE(CONCAT(month, '-01'), '%Y-%m-%d');
