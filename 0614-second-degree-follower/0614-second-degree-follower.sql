# Write your MySQL query statement below

SELECT followee as follower, COUNT(*) as num FROM Follow
WHERE followee in 
(
SELECT distinct F1.follower 
FROM Follow F1
JOIN Follow F2
ON F1.follower = F2.followee
)
GROUP BY 1
ORDER BY 1