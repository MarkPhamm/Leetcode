# Write your MySQL query statement below
WITH CTE AS
(
SELECT 
    fuel_type,
    driver_id,
    ROUND(AVG(rating),2) rating,
    SUM(distance) distance,
    RANK() OVER(PARTITION BY fuel_type ORDER BY AVG(rating) DESC, SUM(distance) DESC, accidents) ranking
FROM Trips
JOIN Vehicles USING(vehicle_id)
JOIN Drivers USING(driver_id)
GROUP BY 1,2
)
SELECT fuel_type, driver_id, rating, distance FROM CTE
WHERE ranking = 1