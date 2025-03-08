# Write your MySQL query statement below
SELECT 
    state, 
    GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') cities,
    SUM(IF(LEFT(city,1) = LEFT(state,1),1,0)) matching_letter_count
FROM cities
GROUP BY 1
HAVING COUNT(city) >= 3
AND matching_letter_count > 0
ORDER BY 3 DESC, 1

