# Write your MySQL query statement below

SELECT
    name as warehouse_name,
    SUM(units*width*length*height) as volume
FROM Warehouse
JOIN Products
USING(product_id)
GROUP BY 1