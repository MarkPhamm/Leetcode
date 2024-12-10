# Write your MySQL query statement below

WITH CTE AS (
    SELECT *, ROW_NUMBER() OVER() AS r FROM CoffeeShop
)

SELECT a.id,
    CASE 
        WHEN a.drink IS NOT NULL THEN a.drink
        ELSE (SELECT drink FROM cte WHERE r<a.r and DRINK IS NOT NULL ORDER BY r DESC limit 1)
    END AS drink
FROM CTE a
