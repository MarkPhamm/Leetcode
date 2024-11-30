# Write your MySQL query statement below

with total_friendships as
(
    SELECT user1_id, user2_id FROM Friendship
    UNION
    SELECT user2_id user1_id, user1_id user2_id FROM Friendship
    ORDER BY 1,2
), 
# finding the pair with common friends
common_friends AS
(
SELECT 
    self.user1_id, 
    others.user2_id,
    COUNT(distinct others.user1_id) common_friend 
FROM total_friendships self
LEFT JOIN total_friendships others
ON self.user2_id = others.user1_id AND self.user1_id < others.user2_id
WHERE others.user2_id IS NOT NULL
GROUP BY 1,2
HAVING COUNT(distinct others.user1_id) >= 3
)
# checking if the 2 are friends
SELECT * FROM common_friends
JOIN total_friendships USING(user1_id, user2_id)