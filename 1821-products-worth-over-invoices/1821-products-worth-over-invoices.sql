# Write your MySQL query statement below

SELECT 
    name,
    IFNULL(SUM(rest),0) as rest,
    IFNULL(SUM(paid),0) as paid,
    IFNULL(SUM(canceled),0) as canceled,
    IFNULL(SUM(refunded),0) as refunded
FROM Product
LEFT JOIN Invoice USING(product_id)
GROUP BY 1
ORDER BY 1