# Write your MySQL query statement below
SELECT seller_id FROM
(
    SELECT 
        seller_id,
        RANK() OVER(ORDER BY SUM(price) DESC) ranking
    FROM Sales
    GROUP BY 1
) a
WHERE ranking = 1
