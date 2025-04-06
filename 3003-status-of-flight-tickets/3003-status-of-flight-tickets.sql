# Write your MySQL query statement below

WITH stg_passengers_flight AS (
    SELECT
        *, 
        RANK() OVER(PARTITION BY flight_id ORDER BY booking_time) ranking
    FROM Passengers
    JOIN Flights USING(flight_id)
)
SELECT 
    passenger_id,
    IF(
        ranking <= capacity, 'Confirmed', 'Waitlist'
    ) Status
FROM stg_passengers_flight
ORDER BY 1
