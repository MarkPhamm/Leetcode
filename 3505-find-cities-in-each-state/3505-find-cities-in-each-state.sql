# Write your MySQL query statement below

SELECT
    state, 
    group_concat(city ORDER BY city SEPARATOR ', ') cities
FROM cities
GROUP BY 1