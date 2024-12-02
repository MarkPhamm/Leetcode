# Write your MySQL query statement below


WITH cte AS (
    SELECT airport, RANK() OVER(ORDER BY SUM(flights_COUNT) DESC) ranking FROM 
    (
    SELECT departure_airport airport, flights_count FROM flights
    UNION ALL
    SELECT arrival_airport airport, flights_count FROM flights
    ) a
    GROUP BY 1
)
SELECT airport airport_id FROM cte
WHERE ranking = 1