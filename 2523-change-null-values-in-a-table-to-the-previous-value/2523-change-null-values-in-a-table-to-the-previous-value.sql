# Write your MySQL query statement below

WITH CTE AS (
    SELECT *, ROW_NUMBER() OVER() AS rnk FROM CoffeeShop
),
CTE2 AS (
    SELECT 
        l.id, l.drink AS left_drink, r.drink AS right_drink, 
        l.rnk, l.rnk - IFNULL(r.rnk, 0) AS diff
    FROM CTE l
    LEFT JOIN CTE r ON r.rnk < l.rnk AND l.drink IS NULL
    WHERE NOT (l.drink IS NULL AND r.drink IS NULL)
)
SELECT id, COALESCE(left_drink, right_drink) AS drink
FROM (
    SELECT *, RANK() OVER(PARTITION BY id ORDER BY diff) AS first FROM CTE2
) a
WHERE first = 1
ORDER BY rnk;
