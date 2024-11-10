# Write your MySQL query statement below
SELECT 
    lower(trim(product_name)) as product_name,
    DATE_FORMAT(sale_date, "%Y-%m") as sale_date,
    COUNT(sale_id) as total
FROM Sales
GROUP BY 1,2
ORDER BY 1,2