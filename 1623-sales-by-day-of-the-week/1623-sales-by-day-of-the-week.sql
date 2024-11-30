# Write your MySQL query statement below
SELECT 
    item_category CATEGORY,
    SUM(IF(DATE_FORMAT(order_date, "%W") = 'Monday', quantity, 0)) MONDAY, 
    SUM(IF(DATE_FORMAT(order_date, "%W") = 'Tuesday', quantity, 0)) TUESDAY, 
    SUM(IF(DATE_FORMAT(order_date, "%W") = 'Wednesday', quantity, 0)) WEDNESDAY, 
    SUM(IF(DATE_FORMAT(order_date, "%W") = 'Thursday', quantity, 0)) THURSDAY, 
    SUM(IF(DATE_FORMAT(order_date, "%W") = 'Friday', quantity, 0)) FRIDAY, 
    SUM(IF(DATE_FORMAT(order_date, "%W") = 'Saturday', quantity, 0)) SATURDAY, 
    SUM(IF(DATE_FORMAT(order_date, "%W") = 'Sunday', quantity, 0)) SUNDAY
FROM Orders
RIGHT JOIN Items USING(item_id)
GROUP BY 1
ORDER BY 1;
