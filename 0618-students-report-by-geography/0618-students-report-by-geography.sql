# Write your MySQL query statement below

-- SELECT 
-- CASE WHEN Continent = 'America' THEN name else null END AS America,
-- CASE WHEN Continent = 'Asia' THEN name else null END AS Asia,
-- CASE WHEN Continent = 'Europe' THEN name else null END AS Europe
-- FROM Student
 
WITH cte as
(
SELECT 
    *, 
    row_number() over(partition by continent order by name) id
FROM Student
)

SELECT 
MAX(CASE WHEN Continent = 'America' THEN name else null END) AS America,
MAX(CASE WHEN Continent = 'Asia' THEN name else null END) AS Asia,
MAX(CASE WHEN Continent = 'Europe' THEN name else null END) AS Europe
FROM cte 
GROUP BY id
ORDER BY id