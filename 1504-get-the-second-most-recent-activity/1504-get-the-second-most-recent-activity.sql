# Write your MySQL query statement below

SELECT username, activity,startDate,endDate FROM
(
    SELECT 
        *,
        RANK() OVER(PARTITION BY username ORDER BY StartDate DESC) ranking,
        COUNT(*) OVER(PARTITION BY username) as activity_count 
    FROM UserActivity
) a
WHERE activity_count = 1
OR ranking = 2