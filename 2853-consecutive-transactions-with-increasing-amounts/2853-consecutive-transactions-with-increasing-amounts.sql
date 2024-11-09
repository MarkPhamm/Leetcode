# Write your MySQL query statement below
WITH cte AS
(
SELECT 
    *,
    LAG(transaction_date) OVER(PARTITION BY customer_id ORDER BY Transaction_date) previous_transaction_date,
    LAG(amount) OVER(PARTITION BY customer_id ORDER BY Transaction_date) previous_amount
FROM Transactions
),
cte2 AS
(
SELECT 
    *,
    CASE 
        WHEN previous_transaction_date IS NULL THEN 1
        WHEN amount <= previous_amount THEN 1
        WHEN previous_transaction_date + INTERVAL 1 DAY != transaction_date THEN 1
        ELSE 0
    END AS start_signal
FROM cte
),
cte3 AS
(
SELECT *, SUM(start_signal) OVER(ORDER BY customer_id, transaction_date) as group_id FROM cte2
)

SELECT customer_id, min(transaction_date) as consecutive_start, max(transaction_date) as consecutive_end
FROM cte3
GROUP BY customer_id, group_id
HAVING COUNT(*) >= 3

