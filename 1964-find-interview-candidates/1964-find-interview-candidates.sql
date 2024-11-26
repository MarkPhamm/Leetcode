# Write your MySQL query statement below

with contests_unpivot as
(
SELECT gold_medal as user_id, contest_id, "gold" as medal FROM Contests
UNION 
SELECT silver_medal as user_id, contest_id, "silver" as medal FROM Contests
UNION 
SELECT bronze_medal as user_id, contest_id, "bronze" as medal FROM Contests
), 
first_citeria as
(
SELECT 
    user_id
FROM contests_unpivot
WHERE medal = 'gold'
GROUP BY user_id
HAVING COUNT(*) >=3
),
second_citeria AS
(
SELECT distinct user_id FROM 
(
SELECT 
    *,
    contest_id - ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY contest_id) group_id
FROM contests_unpivot
) a
GROUP BY user_id, group_id
HAVING COUNT(*) >= 3
)

SELECT name, mail FROM first_citeria
JOIN Users USING(user_id)
UNION 
SELECT name, mail FROM second_citeria
JOIN Users USING(user_id)