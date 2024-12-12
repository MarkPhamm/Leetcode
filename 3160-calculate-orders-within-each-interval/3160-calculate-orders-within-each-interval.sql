-- Write your MySQL query statement below
WITH signals AS (
    SELECT
        *,
        IF(minute % 6 = 1, 1, 0) AS sig
    FROM Orders
), 
interval_nos AS (
    SELECT 
        *,
        SUM(sig) OVER (ORDER BY minute) AS interval_no
    FROM signals
)
SELECT 
    interval_no, 
    SUM(order_count) AS total_orders
FROM interval_nos
GROUP BY interval_no
ORDER BY interval_no;
