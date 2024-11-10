# Write your MySQL query statement below

with total_calls AS
(
    SELECT caller_id as id, duration FROM Calls
    UNION ALL
    SELECT callee_id as id, duration FROM Calls
)

SELECT distinct name as country FROM 
(
SELECT 
    country.name,
    duration,
    avg(duration) over() all_avg,
    avg(duration) over(partition by country.name) country_avg 
FROM total_calls
JOIN Person USING(id)
JOIN Country ON country.country_code = left(phone_number,3)
) a
WHERE country_avg > all_avg