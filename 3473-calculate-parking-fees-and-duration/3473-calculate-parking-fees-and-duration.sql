# Write your MySQL query statement below

WITH most_spent_parking AS
(
    SELECT
        car_id, 
        lot_id,
        RANK() OVER(PARTITION BY car_id ORDER BY SUM(timestampdiff(MINUTE, entry_time, exit_time)/60) DESC) ranking,
        SUM(timestampdiff(MINUTE, entry_time, exit_time)/60) total_time_spent

    FROM ParkingTransactions
    GROUP BY 1,2
)

SELECT 
    car_id,
    SUM(fee_paid) total_fee_paid,
    ROUND(SUM(fee_paid)/SUM(timestampdiff(MINUTE, entry_time, exit_time)/60),2) avg_hourly_fee,
    most_spent_parking.lot_id most_time_lot
FROM ParkingTransactions
JOIN most_spent_parking USING(car_id)
WHERE ranking = 1
GROUP BY 1
ORDER BY 1