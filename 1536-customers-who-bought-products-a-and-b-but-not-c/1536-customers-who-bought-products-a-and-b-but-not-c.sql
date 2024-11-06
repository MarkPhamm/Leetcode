# Write your MySQL query statement below

SELECT customer_id, customer_name FROM Orders
JOIN Customers using(customer_id)
WHERE product_name in ('A','B')
AND customer_id NOT IN (SELECT customer_id FROM Orders WHERE product_name = 'C')
GROUP BY 1,2
HAVING COUNT(distinct product_name) = 2