# Write your MySQL query statement below

SELECT 
    account_id, 
    day,
    SUM(IF(type="Deposit",amount,-amount)) OVER(PARTITION BY account_id ORDER BY day) balance
FROM Transactions 