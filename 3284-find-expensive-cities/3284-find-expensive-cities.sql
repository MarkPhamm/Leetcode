# Write your MySQL query statement below

SELECT distinct city 
FROM
(
SELECT  
    *,
    AVG(price) OVER(PARTITION BY city) city_avg,
    AVG(price) OVER() national_avg
FROM Listings
) a
WHERE city_avg > national_avg
ORDER BY 1