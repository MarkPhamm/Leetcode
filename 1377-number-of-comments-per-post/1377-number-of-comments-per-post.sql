# Write your MySQL query statement below
WITH comments AS
(
SELECT parent_id, COUNT(distinct sub_id) AS number_of_comments
FROM Submissions
WHERE parent_id IS NOT NULL
GROUP BY 1
),
posts AS
(
    SELECT distinct sub_id FROM Submissions
    WHERE parent_id IS NULL    
)
SELECT sub_id as post_id, IFNULL(number_of_comments,0) AS number_of_comments FROM posts
LEFT JOIN comments
ON posts.sub_id = comments.parent_id
ORDER BY 1