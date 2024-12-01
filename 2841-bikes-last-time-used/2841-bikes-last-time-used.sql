# Write your MySQL query statement below
SELECT 
    bike_number,
    MAX(end_time) end_time
FROM Bikes
GROUP BY 1
ORDER BY 2 DESC