# Write your MySQL query statement below

WITH cte AS
(
SELECT 
    customer_id, 
    product_id, 
    RANK() OVER(PARTITION BY customer_id ORDER BY COUNT(distinct order_id) DESC) ranking
FROM Orders
GROUP BY 1,2
)
SELECT customer_id, product_id, product_name FROM cte
JOIN Products
USING(product_id)
WHERE ranking = 1