# Write your MySQL query statement below
SELECT 
    ifnull(
    round(
    count(distinct(concat(requester_id, accepter_id)))/
    count(distinct(concat(sender_id, send_to_id)))
    ,2)
    ,0) as accept_rate
FROM RequestAccepted, FriendRequest