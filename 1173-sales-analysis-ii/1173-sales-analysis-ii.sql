# Write your MySQL query statement below
with cte as
(
    SELECT * FROM Product
    JOIN Sales
    using(product_id)
)

SELECT distinct buyer_id FROM cte
WHERE buyer_id NOT IN (SELECT buyer_id FROM cte WHERE product_name = "Iphone")
AND product_name = 'S8'
ORDER BY 1