# Write your MySQL query statement below

WITH CTE as
(
SELECT 
    box_id,
    chest_id, 
    boxes.apple_count as boxes_apple,
    boxes.orange_count as boxes_orange,
    chests.apple_count as chests_apple,
    chests.orange_count as chests_orange
FROM Boxes
LEFT JOIN Chests
USING(chest_id)
)

SELECT sum(apple) apple_count, sum(orange) orange_count FROM
(
SELECT boxes_apple apple, boxes_orange orange FROM CTE
UNION ALL
SELECT chests_apple apple, chests_orange orange FROM CTE
) a