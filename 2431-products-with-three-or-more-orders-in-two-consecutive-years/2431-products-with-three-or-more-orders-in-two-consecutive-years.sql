# Write your MySQL query statement below

SELECT distinct product_id FROM 
(
SELECT 
    *, 
    LAG(year_purchase) OVER(PARTITION BY product_id ORDER BY year_purchase) prev_year
FROM 
(
SELECT 
    product_id, 
    year(purchase_date) year_purchase,
    COUNT(order_id) total_order
FROM Orders
GROUP BY 1,2
HAVING total_order >= 3
) a
) b
WHERE year_purchase - prev_year = 1