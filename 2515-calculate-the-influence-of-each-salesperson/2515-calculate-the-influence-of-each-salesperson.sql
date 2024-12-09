# Write your MySQL query statement below
WITH customer_sales AS (
    SELECT 
        customer_id, 
        SUM(price) AS total_sales
    FROM Sales
    GROUP BY customer_id
)
SELECT 
    salesperson_id, 
    name, 
    IFNULL(SUM(total_sales), 0) AS total
FROM Salesperson
LEFT JOIN Customer USING (salesperson_id)
LEFT JOIN customer_sales USING (customer_id)
GROUP BY salesperson_id, name;
