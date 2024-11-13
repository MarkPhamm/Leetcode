# Write your MySQL query statement below
SELECT * FROM
(
SELECT 
    sale_date,
    sold_num - LEAD(sold_num) OVER(PARTITION BY sale_date ORDER BY sale_date, fruit)  diff    
FROM Sales
) a
WHERE diff is not null