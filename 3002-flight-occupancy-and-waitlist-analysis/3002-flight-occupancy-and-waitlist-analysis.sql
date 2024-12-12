# Write your MySQL query statement below
with customer_booking AS
(
SELECT
    flight_id, 
    COUNT(passenger_id) total_booking
FROM passengers
GROUP BY 1
)
SELECT 
    flight_id, 
    IFNULL(IF(total_booking>capacity, capacity, total_booking),0) booked_cnt,
    IFNULL(IF(total_booking>capacity, total_booking - capacity, 0),0) waitlist_cnt
FROM Flights
LEFT JOIN customer_booking USING(flight_id)
ORDER BY 1