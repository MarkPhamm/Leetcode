# Write your MySQL query statement below
SELECT city_id, day, degree FROM 
(
SELECT 
    *,
    RANK() OVER(PARTITION BY city_id ORDER BY degree DESC, day) rnk
FROM Weather
) a
WHERE rnk = 1