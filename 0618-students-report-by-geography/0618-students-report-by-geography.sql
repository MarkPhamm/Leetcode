# Write your MySQL query statement below

-- SELECT 
-- CASE WHEN Continent = 'America' THEN name else null END AS America,
-- CASE WHEN Continent = 'Asia' THEN name else null END AS Asia,
-- CASE WHEN Continent = 'Europe' THEN name else null END AS Europe
-- FROM Student
with america as
(
SELECT 
    row_number() over(ORDER BY name) as id,
    name as America
FROM Student
WHERE continent = 'America'
),

asia as
(
SELECT 
    row_number() over(ORDER BY name) as id,
    name as Asia
FROM Student
WHERE continent = 'Asia'
),

europe as
(
SELECT 
    row_number() over(ORDER BY name) as id,
    name as Europe
FROM Student
WHERE continent = 'Europe'
)

SELECT America, Asia, Europe FROM america
LEFT JOIN asia using(id)
LEFT JOIN europe using(id)