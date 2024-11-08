# Write your MySQL query statement below

SELECT 
    customer_id, 
    name
FROM 
(
SELECT 
    customer_id, 
    name,
    DATE_FORMAT(order_date,'%Y-%m') as month_year,
    SUM(Quantity*Price) as spent
FROM Orders
JOIN Product USING(product_id)
JOIN Customers USING(customer_id)
WHERE DATE_FORMAT(order_date,'%Y-%m') in ("2020-06","2020-07")
GROUP BY 1,2,3
HAVING spent >= 100
) a
GROUP BY 1,2
HAVING COUNT(distinct month_year) >= 2