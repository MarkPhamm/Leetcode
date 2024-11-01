# Write your MySQL query statement below
SELECT product_id, sum(quantity) as total_quantity FROM Sales
GROUP BY 1