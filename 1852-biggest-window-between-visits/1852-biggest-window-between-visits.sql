# Write your MySQL query statement below

WITH next_visits AS
(
SELECT 
    *,
    IFNULL(LEAD(visit_date) OVER(partition by user_id ORDER BY visit_date),'2021-01-01') next_visit
FROM UserVisits
)

SELECT user_id, diff_window as biggest_window FROM 
(
SELECT 
    *,
    DATEDIFF(next_visit, visit_date) diff_window,
    ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY DATEDIFF(next_visit, visit_date) DESC)  ranking 
FROM next_visits
) a
WHERE ranking = 1