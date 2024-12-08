# Write your MySQL query statement below

SELECT user_id, product_id FROM 
(
SELECT user_id, product_id, RANK() OVER(PARTITION BY user_id ORDER BY SUM(quantity*price) DESC) ranking FROM Sales
LEFT JOIN Product USING(product_id)
GROUP BY 1,2
) a
WHERE ranking = 1