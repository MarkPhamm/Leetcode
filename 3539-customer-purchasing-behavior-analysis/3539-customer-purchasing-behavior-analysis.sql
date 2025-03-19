# Write your MySQL query statement below

WITH cte AS
(
SELECT 
    customer_id,
    ROUND(SUM(amount),2) total_amount,
    COUNT(transaction_id) transaction_count,
    COUNT(DISTINCT category) unique_categories,
    ROUND(AVG(amount),2) avg_transaction_amount,
    ROUND(COUNT(transaction_id)*10 + (SUM(amount)/100),2) loyalty_score
FROM Transactions
JOIN Products USING(product_id)
GROUP BY 1
),

ranking_aggregrate_user_category AS
(
SELECT 
    customer_id, 
    category ,
    -- COUNT(*),
    -- MAX(transaction_date) max_transaction_date,
    RANK() OVER(PARTITION BY customer_id ORDER BY COUNT(*) DESC, MAX(transaction_date) DESC) ranking
FROM Transactions
JOIN Products USING(product_id)
GROUP BY 1, 2
)

SELECT 
    customer_id,
    total_amount,
    transaction_count, 
    unique_categories, 
    avg_transaction_amount,
    category top_category,
    loyalty_score
FROM ranking_aggregrate_user_category
JOIN cte USING(customer_id)
WHERE ranking = 1
ORDER BY loyalty_score DESC, customer_id