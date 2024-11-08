# Write your MySQL query statement below
SELECT 
    customer_id, 
    name
FROM Orders
JOIN Product USING(product_id)
JOIN Customers USING(customer_id)
WHERE DATE_FORMAT(order_date,'%Y-%m') in ("2020-06","2020-07")
GROUP BY 1,2
HAVING SUM(IF(order_date LIKE '2020-06%', quantity * price, 0)) >= 100
AND SUM(IF(order_date LIKE '2020-07%', quantity * price, 0)) >= 100
