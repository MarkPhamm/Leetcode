# Write your MySQL query statement below
SELECT 
    bus_id, SUM(IF(ranking = 1 AND passengers_arrival_time IS NOT NULL,1,0)) passengers_cnt
FROM 
(
    SELECT 
        bus_id, 
        Buses.arrival_time bus_arrival_time,
        Passengers.arrival_time passengers_arrival_time,
        RANK() OVER(PARTITION BY passenger_id ORDER BY Buses.arrival_time) ranking
    FROM Buses
    LEFT JOIN Passengers
    ON Buses.arrival_time >= Passengers.arrival_time
) a
GROUP BY 1
ORDER BY 1