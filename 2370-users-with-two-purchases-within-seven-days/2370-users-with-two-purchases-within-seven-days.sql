# Write your MySQL query statement below
SELECT distinct user_id FROM 
(
SELECT 
    user_id, 
    DATEDIFF(lead(purchase_date) OVER(PARTITION BY user_id ORDER BY purchase_date), purchase_date) diff
FROM Purchases 
) a
WHERE diff <= 7
ORDER BY user_id