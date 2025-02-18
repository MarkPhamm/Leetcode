# Write your MySQL query statement below
WITH cte AS (
    SELECT *, 
    LAG(spend,2) OVER(PARTITION BY user_id ORDER BY transaction_date) first_spend,
    LAG(spend) OVER(PARTITION BY user_id ORDER BY transaction_date) second_spend,
    DENSE_RANK() OVER(PARTITION BY user_id ORDER BY transaction_date) time_ranking
    FROM Transactions
)

SELECT user_id, spend third_transaction_spend, transaction_date third_transaction_date  FROM cte
WHERE time_ranking = 3 AND spend > first_spend AND spend > second_spend
ORDER BY user_id
