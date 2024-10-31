# Write your MySQL query statement below

SELECT seat_id FROM 
(
SELECT 
    seat_id, 
    LAG(seat_id) OVER() as prev,
    LEAD(seat_id) OVER() as next
FROM Cinema
WHERE free = 1
) a
WHERE seat_id = next-1
or seat_id = prev+1

