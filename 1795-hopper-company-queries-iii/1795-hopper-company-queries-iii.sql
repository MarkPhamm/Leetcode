# Write your MySQL query statement below


WITH recursive months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM months
    WHERE month < 12
),
aggregrate_months as
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

filling_zero as
(
SELECT 
    month, 
    CASE WHEN ride_distance IS NULL THEN 0 ELSE ride_distance END as ride_distance,
    CASE WHEN ride_duration IS NULL THEN 0 ELSE ride_duration END as ride_duration
FROM months
LEFT JOIN aggregrate_months
USING(month)
)

SELECT * FROM 
(
SELECT 
    month,
    ROUND(SUM(ride_distance) OVER(order by month range between current row and 2 Following)/3,2) as average_ride_distance,
    ROUND(SUM(ride_duration) OVER(order by month range between current row and 2 Following)/3,2) as average_ride_duration
FROM filling_zero
) a
WHERE month <= 10