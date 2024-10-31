# Write your MySQL query statement below

SELECT 
    min(round(sqrt(pow((d1.x-d2.x),2) + pow((d1.y-d2.y),2)),2)) as shortest 
FROM Point2D d1
JOIN Point2D d2
WHERE d1.x != d2.x
OR d1.y != d2.y