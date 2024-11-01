# Write your MySQL query statement below
-- SELECT 
--     month(requested_at) as month,
--     SUM(ride_distance) OVER(order by month(requested_at) range between current row and 2 Following)/3 as average_ride_distance,
--     SUM(ride_duration) OVER(order by month(requested_at) range between current row and 2 Following)/3 as average_ride_duration
-- FROM AcceptedRides
-- LEFT JOIN Rides USING(ride_id)
-- WHERE year(requested_at) = 2020

WITH cte AS (
SELECT 1 AS month
UNION
SELECT 2
UNION
SELECT 3
UNION
SELECT 4
UNION
SELECT 5
UNION
SELECT 6
UNION
SELECT 7
UNION
SELECT 8
UNION
SELECT 9
UNION
SELECT 10
UNION
SELECT 11
UNION
SELECT 12
),
cte2 as
(
SELECT 
    month(requested_at) as month,
    SUM(ride_distance) as ride_distance,
    SUM(ride_duration) as ride_duration
FROM AcceptedRides
LEFT JOIN Rides USING(ride_id)
WHERE year(requested_at) = 2020
GROUP BY 1
),

cte3 as
(
SELECT 
    month, 
    CASE WHEN ride_distance IS NULL THEN 0 ELSE ride_distance END as ride_distance,
    CASE WHEN ride_duration IS NULL THEN 0 ELSE ride_duration END as ride_duration
FROM cte 
LEFT JOIN cte2
USING(month)
)

SELECT * FROM 
(
SELECT 
    month,
    ROUND(SUM(ride_distance) OVER(order by month range between current row and 2 Following)/3,2) as average_ride_distance,
    ROUND(SUM(ride_duration) OVER(order by month range between current row and 2 Following)/3,2) as average_ride_duration
FROM cte3
) a
WHERE month <= 10