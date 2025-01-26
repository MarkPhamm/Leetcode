# Write your MySQL query statement below
WITH CTE as
(
SELECT seller_id, COUNT(distinct item_id) num_items FROM Orders
JOIN Users USING(seller_id)
JOIN Items USING(item_id)
WHERE item_brand != favorite_brand
GROUP BY 1
)

SELECT seller_id, num_items FROM
(
SELECT *, RANK() OVER(ORDER BY num_items DESC) ranking FROM CTE
) a
WHERE ranking = 1
ORDER BY 1