# Write your MySQL query statement below

SELECT 
    (day(purchase_date)+4)/7 week_of_month,
    purchase_date, 
    SUM(amount_spend) total_amount
FROM purchases
WHERE weekday(purchase_date) = 4 AND purchase_date BETWEEN '2023-11-01' AND '2023-11-30'
GROUP BY 1,2
ORDER BY 1,2