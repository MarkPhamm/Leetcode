# Write your MySQL query statement below
WITH available_books AS
(
    SELECT * FROM Books
    WHERE available_from < "2019-06-23" - INTERVAL 1 MONTH
),
valid_orders AS
(
    SELECT * FROM orders
    WHERE dispatch_date between "2019-06-23" - INTERVAL 1 YEAR AND "2019-06-23" 
)

SELECT 
    Available_books.book_id, 
    name
FROM Available_books
LEFT JOIN valid_orders
USING(book_id)
GROUP BY 1,2
HAVING SUM(quantity) < 10 OR SUM(Quantity) IS NULL