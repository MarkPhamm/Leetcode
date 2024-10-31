# Write your MySQL query statement below

SELECT followee AS follower, COUNT(followee) AS num
FROM Follow
WHERE followee IN (
    SELECT follower 
    FROM Follow
)
GROUP BY 1
ORDER BY 1 ASC