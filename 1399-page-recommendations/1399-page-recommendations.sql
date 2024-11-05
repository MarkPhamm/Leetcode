# Write your MySQL query statement below
WITH friend_list AS
(
SELECT user2_id as friend_id FROM Friendship
WHERE user1_id = 1
UNION
SELECT user1_id as friend_id FROM Friendship
WHERE user2_id = 1
) 

SELECT distinct page_id AS recommended_page FROM friend_list
JOIN Likes
ON friend_list.friend_id = Likes.user_id
WHERE page_id not IN (SELECT distinct page_id FROM Likes WHERE user_id = 1)