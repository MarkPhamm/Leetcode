# Write your MySQL query statement below
SELECT distinct a.account_id FROM Loginfo a
LEFT JOIN Loginfo b 
ON a.account_id = b.account_id
AND a.ip_address != b.ip_address
AND b.login between a.login and a.logout
WHERE b.account_id IS NOT NULL