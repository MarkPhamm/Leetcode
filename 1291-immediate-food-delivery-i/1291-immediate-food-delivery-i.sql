# Write your MySQL query statement below

SELECT
ROUND(COUNT(DISTINCT IF(order_date = customer_pref_delivery_date, delivery_id, null))/COUNT(DISTINCT delivery_id)*100,2) AS immediate_percentage 
FROM Delivery